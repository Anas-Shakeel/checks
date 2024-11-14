""" Core CLI loop, parsing commands and routing """

import sys
from checks.parser import Parser
from checks.exceptions import ParseError
from checks.commands import (
    add,
    check,
    check_all,
    uncheck,
    uncheck_all,
    delete,
    list_tasks,
    search,
    clear,
    save
)


PROGRAM = "checks"
VERSION = "0.1"


def main():
    """ The Interactive CLI Session """

    print("%s version %s" % (PROGRAM.title(), VERSION))
    print("Type 'help' for usage hint. (CTRL+C to force quit)\n")

    try:
        while True:
            command = input("checks> ").strip()
            # Empty?
            if not command:
                continue

            # Parse and process the command
            process_command(command)

    except (KeyboardInterrupt, EOFError):
        print("Force quit.")
        sys.exit(0)


def process_command(command: str):
    """ Process command using `Parser` class """
    # Parse the command
    try:
        tokens = Parser.parse(command)
    except ParseError as e:
        print("Parse error: %s" % e)
        return

    match tokens['action']:
        case "help":
            print_help()

        case "add":
            add(tokens['args'])

        case "check":
            flags = tokens['flags']
            if "-a" in flags or "--all" in flags:
                check_all()
                return

            check(tokens['args'])

        case "uncheck":
            flags = tokens['flags']
            if "-a" in flags or "--all" in flags:
                uncheck_all()
                return

            uncheck(tokens['args'])

        case "delete":
            flags = tokens['flags']
            if "-a" in flags or "--all" in flags:
                clear()
                return

            delete(tokens['args'])

        case "list":
            flags = tokens['flags']
            minimal = "-m" in flags or "--minimal" in flags
            completed = "-c" in flags or "--completed" in flags
            pending = "-p" in flags or "--pending" in flags

            list_tasks(completed=completed, pending=pending, minimal=minimal)

        case "search":
            search(tokens['args'][0])

        case "save":
            save()

        case "exit":
            sys.exit(0)

        case _:
            print("Unknown command.")


def print_help():
    """ Print help text """
    print("Help is on the way, Hang tight!")
