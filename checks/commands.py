from checks.db.json_database import db
from tabulate import tabulate


def list_tasks():
    """ Print all tasks all tasks in a tabular format """
    tasks = [task.to_dict() for task in db.list_tasks()]
    if not tasks:
        print("No tasks.")
        return
    headers = {k: k.upper().replace("_", " ") for k in tasks[0].keys()}
    print(tabulate(tasks, headers=headers, tablefmt="simple_outline"))
