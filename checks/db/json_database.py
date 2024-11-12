""" JSON handling for working with json database """

import json
from pathlib import Path
from checks.models import Task
from checks.utils import get_current_datetime

from typing import List

DB_PATH = Path("tasks.json")


class Database:
    def __init__(self, db_path: Path = DB_PATH) -> None:
        self.db_path = db_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
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
            json.dump([task.to_dict() for task in self.tasks], file, indent=2)


# Import this as database
db = Database()
