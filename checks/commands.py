from checks.db.json_database import db
from tabulate import tabulate


def add(descriptions):
    """ Add tasks into the database. Multiple tasks supported. """
    if not descriptions:
        print("No tasks were added.")
        return

    if isinstance(descriptions, str):
        # Add single task
        db.add_task(descriptions)
        print("Task added: '%s'" % descriptions)
    else:
        # Add bulk tasks
        count = db.add_tasks(descriptions)
        if not count:
            print("No tasks added.")
            return
        print("%d Tasks added." % count)


def check(task_ids):
    """ Mark tasks as completed. """
    if isinstance(task_ids, int):
        task = db.check_task(task_ids)
        if not task:
            print("No task with ID: %d", task_ids)
            return
        print("Task checked: '%s'" % task.description)
    else:
        count = db.check_tasks(task_ids)
        if not count:
            print("No tasks checked.")
            return
        print("%d Tasks checked." % count)


def list_tasks():
    """ Print all tasks all tasks in a tabular format """
    tasks = [task.to_dict() for task in db.list_tasks()]
    if not tasks:
        print("No tasks.")
        return
    headers = {k: k.upper().replace("_", " ") for k in tasks[0].keys()}
    print(tabulate(tasks, headers=headers, tablefmt="simple_outline"))
