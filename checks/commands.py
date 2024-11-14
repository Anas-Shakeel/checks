from checks.db.json_database import db
from checks.models import Task
from tabulate import tabulate
from utils import pins, DATE_FORMAT
from typing import List


def add(descriptions):
    """ Add tasks into the database. Multiple tasks supported. """
    if not descriptions:
        print("No tasks were added.")
        return

    if len(descriptions) == 1:
        # Add single task
        db.add_task(descriptions[0])
        print("Task added: '%s'" % descriptions[0])
    else:
        # Add bulk tasks
        count = db.add_tasks(descriptions)
        if not count:
            print("No tasks added.")
            return
        print("%d Tasks added." % count)


def check(task_ids):
    """ Mark tasks as complete. """
    if len(task_ids) == 1:
        task = db.check_task(task_ids[0])
        if not task:
            print("No task with ID: %d" % task_ids[0])
            return
        print("Task checked: '%s'" % task.description)
    else:
        count = db.check_tasks(task_ids)
        if not count:
            print("No tasks checked.")
            return
        print("%d Tasks checked." % count)


def check_all():
    count = db.check_all()
    print("%d tasks checked." % count)


def uncheck(task_ids):
    """ Mark tasks as incomplete. """
    if len(task_ids) == 1:
        task = db.uncheck_task(task_ids[0])
        if not task:
            print("No task with ID: %d" % task_ids[0])
            return
        print("Task unchecked: '%s'" % task.description)
    else:
        count = db.uncheck_tasks(task_ids)
        if not count:
            print("No tasks unchecked.")
            return
        print("%d Tasks unchecked." % count)


def uncheck_all():
    count = db.uncheck_all()
    print("%d tasks unchecked." % count)


def delete(task_ids):
    """ Delete tasks from database. """
    if len(task_ids) == 1:
        task = db.delete_task(task_ids[0])
        if not task:
            print("No task with ID: %d" % task_ids[0])
            return
        print("Task deleted: '%s'" % task.description)
    else:
        count = db.delete_tasks(task_ids)
        if not count:
            print("No tasks deleted.")
            return
        print("%d Tasks deleted." % count)


def clear(delete_file: bool = False):
    """ Clear the database. Delete everything in it. """
    db.clear_database(delete_file)
    print("Database cleared.")


def list_tasks(completed: bool = False, pending: bool = False, minimal: bool = False):
    """ Print all tasks all tasks in a tabular format. """
    if completed:
        tasks = [task for task in db.list_tasks() if task.completed]
    elif pending:
        tasks = [task for task in db.list_tasks() if not task.completed]
    else:
        tasks = list(db.list_tasks())

    if not tasks:
        print("No tasks.")
        return

    only = None
    if minimal:
        only = ['id', 'description']

    tasks = normalize(tasks, only=only)
    headers = normalize_headers(tasks[0].keys())
    table_fmt = "presto" if minimal else "simple_outline"

    print(tabulate(tasks, headers=headers, tablefmt=table_fmt))


def normalize(tasks: List[Task], only=None):
    """ Normalize tasks for pretty-print """
    keys = set(tasks[0].to_dict().keys())
    intersection = None

    if only:
        only = set(only)
        intersection = keys.intersection(only)

    keys = intersection if intersection else keys

    new_tasks = []
    for task in sorted(tasks, key=lambda t: not t.completed):
        color = "dark_grey" if task.completed else "green"
        status = "Completed" if task.completed else "Pending"
        create_date = pins.time_ago(task.created_at, DATE_FORMAT)
        complete_date = pins.time_ago(task.completed_at,
                                      DATE_FORMAT) if task.completed_at else None

        new_task = {}
        if "id" in keys:
            new_task["id"] = pins.colorize(task.id, fgcolor=color)
        if "description" in keys:
            new_task["description"] = pins.colorize(
                task.description, fgcolor=color)
        if "completed" in keys:
            new_task["status"] = pins.colorize(status, fgcolor=color)
        if "created_at" in keys:
            new_task["created"] = pins.colorize(create_date, fgcolor=color)
        if "completed_at" in keys:
            pins.colorize(complete_date, fgcolor=color)

        if new_task:
            new_tasks.append(new_task)

    return new_tasks


def normalize_headers(headers):
    """ Normalize headers for use in tabulate tables """
    return {k: k.title().replace("_", " ") for k in headers}


def search(keyword: str):
    """ Search tasks using keyword in task's description. """
    tasks = [task for task in db.search_tasks(keyword)]
    if not tasks:
        print("No tasks found.")
        return
    tasks = normalize(tasks)
    headers = normalize_headers(tasks[0].keys())
    print(tabulate(tasks, headers=headers, tablefmt="simple_outline"))


def save():
    """ Save the database in it's current state. """
    db.save_tasks()
    print("Database saved.")
