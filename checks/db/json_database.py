""" JSON handling for working with json database """

import json
from pathlib import Path

DB_PATH = Path("tasks.json")


def load_tasks():
    """ Read & load json file, Returns the json data as python object """
    if DB_PATH.exists():
        with open(DB_PATH, "r", encoding="utf-8") as file:
            return json.load(file)


def save_tasks(tasks):
    pass
