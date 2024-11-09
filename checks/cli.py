""" Core CLI loop, parsing commands and routing """

import sys
from checks.cmd_parser import Parser
from checks.commands import add, check, uncheck, delete, list_tasks
from checks.db.json_database import load_tasks, save_tasks


def main():
    """ The Interactive CLI Session """

    print("Welcome to Checks cli!")
    print("Type 'help' for a list of commands.")

    try:
        while True:
            command = input("\nchecks> ").strip()
            if command == "help":
                print_help()
            else:
                process_command(command)
    except (KeyboardInterrupt, EOFError):
        print("Force quit.")
        sys.exit(0)
    except ValueError:
        print("CLI: An unknown error occured.")
        sys.exit(1)


def process_command(command: str):
    """ Process command using `Parser` class """
    # Parse the command
    Parser.parse(command)


def print_help():
    """ Print help text """
    print("Help is on the way, Hang tight!")
