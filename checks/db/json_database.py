""" JSON handling for working with json database """

import json
from pathlib import Path
from checks.models import Task
from checks.utils import get_current_datetime

from typing import List, Dict, Union, Iterable, Optional

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
        self.tasks: Dict[int, Task] = self.load_tasks()

    def load_tasks(self) -> Dict[int, dict]:
        """ Load tasks from JSON file into memory. """
        if self.db_path.exists():
            try:
                with open(self.db_path, "r", encoding="utf-8") as file:
                    tasks_data = json.load(file)

                # Load into memory as dict for quick lookup
                return {data["id"]: Task.from_dict(data) for data in tasks_data}
            except json.JSONDecodeError:
                pass
        return {}

    def save_tasks(self):
        """ Saves tasks from memory to JSON file. """
        if not self.tasks:
            return

        with open(self.db_path, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks.values()],
                      file, indent=2)

    def add_task(self, description: str) -> Task:
        """ Add a new task to in-memory database and save the database """
        new_task = Task(description=description)
        self.tasks[new_task.id] = new_task
        self.save_tasks()
        return new_task

    def add_tasks(self, descriptions: Iterable[str]):
        """ Add bulk tasks into in-memory database efficiently. """
        # Create & Add tasks to db
        for desc in descriptions:
            new_task = Task(description=desc)
            self.tasks[new_task.id] = new_task

        self.save_tasks()

    def get_task(self, task_id: int) -> Optional[Task]:
        """ Returns a task by it's ID """
        return self.tasks.get(task_id, None)

    def check_task(self, task_id: int) -> Optional[Task]:
        """ Mark a task as completed, Returns the task if succeed,
        `None` if task_id wasn't found """
        task = self.get_task(task_id)
        if task and not task.completed:
            task.completed = True
            task.completed_at = get_current_datetime()
            self.save_tasks()
        return task

    def check_tasks(self, task_ids: int):
        """ Mark bulk tasks as completed. """
        datetime = get_current_datetime()
        for id_ in task_ids:
            task = self.get_task(id_)
            if task and not task.completed:
                task.completed = True
                task.completed_at = datetime
        self.save_tasks()
        return task

    def uncheck_task(self, task_id: int) -> Optional[Task]:
        """ Mark a task as incomplete, Returns the task if succeed,
        `None` if task_id wasn't found """
        task = self.get_task(task_id)
        if task and task.completed:
            task.completed = False
            task.completed_at = None
            self.save_tasks()
        return task

    def uncheck_tasks(self, task_ids: int):
        """ Mark bulk tasks as incomplete. """
        for id_ in task_ids:
            task = self.get_task(id_)
            if task and task.completed:
                task.completed = False
                task.completed_at = None
        self.save_tasks()
        return task

    def __str__(self) -> str:
        string = ""
        for task in self.tasks.values():
            string += f"{task}\n"

        return string.rstrip()


# Import this as database
db = Database()
