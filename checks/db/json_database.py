""" JSON handling for working with json database """

import json
from pathlib import Path
from checks.models import Task
from checks.utils import get_current_datetime

from typing import List

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


def save_tasks(tasks: List[Task]):
    """ Save/Write `tasks` to json file/database """
    if not tasks:
        return

    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=2)


def add_task(description: str) -> Task:
    """ Add a new task `description` to the database. Returns the new task """
    tasks = load_tasks()

    new_task = Task(description=description)
    tasks.append(new_task)
    save_tasks(tasks)

    return new_task
