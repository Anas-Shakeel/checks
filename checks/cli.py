""" Core CLI loop, parsing commands and routing """

import sys
from checks.parser import Parser
from checks.exceptions import ParseError
from checks.utils import pins, err
from checks.commands import (
    add,
    check,
    check_all,
    uncheck,
    uncheck_all,
    remove,
    list_tasks,
    search,
    remove_all,
    save,
    clear
)


PROGRAM = "checks"
VERSION = "0.1"


def main():
    """ The Interactive CLI Session """
    print_startup_info()

    PROMPT = pins.colorize("@checks/> ", "sea_green", attrs=['italic'])

    try:
        while True:
            command = input(PROMPT).strip()
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

        case "add" | "a":
            add(tokens['args'])

        case "check" | "c":
            flags = tokens['flags']
            if "-a" in flags or "--all" in flags:
                check_all()
                return

            check(tokens['args'])

        case "uncheck" | "uc":
            flags = tokens['flags']
            if "-a" in flags or "--all" in flags:
                uncheck_all()
                return

            uncheck(tokens['args'])

        case "remove" | "rm":
            flags = tokens['flags']
            if "-a" in flags or "--all" in flags:
                agree = pins.input_question("Remove all tasks? (y/N): ",
                                            prompt_color="light_red")
                if agree:
                    remove_all()
                return

            remove(tokens['args'])

        case "list" | "ls":
            flags = tokens['flags']
            minimal = "-m" in flags or "--minimal" in flags
            completed = "-c" in flags or "--completed" in flags
            pending = "-p" in flags or "--pending" in flags

            list_tasks(completed=completed, pending=pending, minimal=minimal)

        case "search" | "sr":
            search(tokens['args'][0])

        case "clear" | "cls":
            clear()

        case "save":
            save()

        case "exit":
            sys.exit(0)

        case _:
            err("CLI Error", "command '%s' is recognized by the parser but not by CLI." %
                tokens["action"])


def print_startup_info():
    """ Print the startup help text. """
    print("%s version %s" % (PROGRAM.title(), VERSION))
    print("Type '%s' for usage hint. (%s to force quit)\n" % (pins.colorize("help", fgcolor="plum"),
                                                              pins.colorize("CTRL+C", fgcolor="light_red")))


def print_help():
    """ Print help text """
    help_table = {
        "add": "add tasks",
        "check": "mark tasks as complete",
        "uncheck": "mark tasks as incomplete",
        "remove": "remove tasks",
        "list": "list all tasks",
        "search": "search tasks",
        "clear": "clear terminal",
        "save": "save all tasks",
        "exit": "exit the application",
        "help": "print this help text",
    }

    print(pins.create_table(help_table, indent_values=4,
                            keys_fg="plum", values_attrs=['italic']))
    print()
