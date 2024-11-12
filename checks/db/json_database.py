""" JSON handling for working with json database """

import json
from pathlib import Path

DB_PATH = Path("tasks.json")


def load_tasks():
    """ Read & load json file, Returns the json data as python object """
    if DB_PATH.exists():
        try:
            with open(DB_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            pass
    return []


def save_tasks(tasks):
    """ Save/Write `tasks` to json file/database """
    if not tasks:
        return
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)
