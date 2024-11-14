from checks.db.json_database import db
from tabulate import tabulate


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
    if isinstance(task_ids, int):
        task = db.delete_task(task_ids)
        if not task:
            print("No task with ID: %d" % task_ids)
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
        tasks = [task.to_dict() for task in db.list_tasks() if task.completed]
    elif pending:
        tasks = [task.to_dict()
                 for task in db.list_tasks() if not task.completed]
    else:
        tasks = [task.to_dict() for task in db.list_tasks()]

    if not tasks:
        print("No tasks.")
        return
    headers = {k: k.upper().replace("_", " ") for k in tasks[0].keys()}
    print(tabulate(tasks, headers=headers, tablefmt="simple_outline"))


def search(keyword: str):
    """ Search tasks using keyword in task's description. """
    tasks = [task.to_dict() for task in db.search_tasks(keyword)]
    if not tasks:
        print("No tasks found.")
        return

    headers = {k: k.upper().replace("_", " ") for k in tasks[0].keys()}
    print(tabulate(tasks, headers=headers, tablefmt="simple_outline"))


def save():
    """ Save the database in it's current state. """
    db.save_tasks()
    print("Database saved.")
