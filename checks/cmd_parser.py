""" Contains a parser that parses commands from user inputs """

import re
from checks.commands import add, check, uncheck, delete, list_tasks

CMD_REGEX = {
    "add": re.compile(r"\".+\""),
    "search": re.compile(r"\".+\""),
    "check": re.compile(r""),
    "uncheck": re.compile(r""),
    "list": re.compile(r""),
    "delete": re.compile(r""),
}


class Parser:
    @classmethod
    def parse(cls, command: str):
        """ Parses a command, Returns tokens `list` """
        # print("Parsing command: '%s'" % command)

        # Tokenize the command
        tokens: tuple = cls.tokenize(command)
        if not tokens:
            return None

        print(tokens)
        return

        return {
            "subcommand": tokens[0],
            "args": tokens[1],
            "flags": tokens[2]
        }

    @classmethod
    def tokenize(cls, command: str):
        """ `command` tokenizer, returns tokens """
        action, args = command.strip().split(" ", 1)

        match action:
            case "add":
                if matches := re.fullmatch(CMD_REGEX['add'], args):
                    return matches.group(0)

                print("invalid syntax: '%s'" % args)
                return None

            case "check":
                pass
            case "uncheck":
                pass
            case "delete":
                pass
            case "list":
                pass
            case _:
                print("unknown command: '%s'" % action)
                return None

        # TEMPORARY: remove afterwards
        return action, args
