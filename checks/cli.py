""" Core CLI loop, parsing commands and routing """

import sys
from checks.cmd_parser import Parser
from checks.commands import add, check, uncheck, delete, list_tasks
from checks.db.json_database import load_tasks, save_tasks
from checks.exceptions import ParseError


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

    print(tokens)


def print_help():
    """ Print help text """
    print("Help is on the way, Hang tight!")
