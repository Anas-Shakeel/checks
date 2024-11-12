""" JSON handling for working with json database """

import json
from pathlib import Path
from checks.models import Task
from checks.utils import get_current_datetime

DB_PATH = Path("tasks.json")


def load_tasks():
    """ load tasks from JSON file, Return tasks as python `list` """
    if DB_PATH.exists():
        try:
            with open(DB_PATH, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
            tasks = [Task.from_dict(data) for data in tasks_data]
            return tasks
        except json.JSONDecodeError:
            pass
    return []


def save_tasks(tasks):
    """ Save/Write `tasks` to json file/database """
    if not tasks:
        return
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)
