""" JSON handling for working with json database """

import json
from pathlib import Path
from checks.models import Task
from checks.utils import get_current_datetime

from typing import List, Dict

DB_PATH = Path("tasks.json")


class Database:
    """ 
    ### Database
    It is an in-memory json database that loads up the tasks JSON file.

    #### Database Data Structure:
    Note that data structure is a bit different in `in-memory` database, compared to
    the `tasks.json` JSON file. This is to support quick lookup using Task IDs.

    #### Exmaple:
    ```
    # A Task in tasks.json
    [
        {
            "id": "1",
            "description": "This is a task.",
            "completed": false,
            "created_at": "12-11-2024 12:48:30",
            "completed_at": null,
        },
        ...
    ]

    # A Task in in-memory database
    {
        1: {
            "id": "1",
            "description": "This is a task.",
            "completed": false,
            "created_at": "12-11-2024 12:48:30",
            "completed_at": null,
        },
        ...
    }
    ```

    """

    def __init__(self, db_path: Path = DB_PATH) -> None:
        self.db_path = db_path

        # Convert to dict with IDs as keys for quick lookup
        self.tasks: Dict[int, Task] = {
            task.id: task for task in self.load_tasks()}

    def load_tasks(self) -> Dict:
        """ Load tasks from JSON file into memory. """
        if self.db_path.exists():
            try:
                with open(self.db_path, "r", encoding="utf-8") as file:
                    tasks_data = json.load(file)
                tasks = [Task.from_dict(data) for data in tasks_data]
                return tasks
            except json.JSONDecodeError:
                pass
        return []

    def save_tasks(self):
        """ Saves tasks from memory to JSON file. """
        if not self.tasks:
            return

        with open(self.db_path, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks.values()],
                      file, indent=2)

    def add_task(self, description: str) -> Task:
        """ Add a new task to in-memory database and save """
        new_task = Task(description=description)
        self.tasks[new_task.id] = new_task
        self.save_tasks()
        return new_task

    def __str__(self) -> str:
        string = ""
        for task in self.tasks.values():
            string += f"{task}\n"

        return string.rstrip()


# Import this as database
db = Database()
