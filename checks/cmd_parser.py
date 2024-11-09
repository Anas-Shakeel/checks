""" Contains a parser that parses commands from user inputs """

import re
# from checks.commands import add, search, check, uncheck, delete, list_tasks
from checks.exceptions import ParseError

CMD_REGEX = {
    "add": re.compile(r"\"(.+)\""),
    "search": re.compile(r"\"(.+)\""),
    "check": re.compile(r""),
    "uncheck": re.compile(r""),
    "list": re.compile(r""),
    "delete": re.compile(r""),
}


class Parser:
    @classmethod
    def parse(cls, command: str):
        """ Parses a command, Returns tokens `list` """
        # Tokenize the command
        return cls.tokenize(command)

    @classmethod
    def tokenize(cls, command: str) -> dict:
        """ `command` tokenizer, returns tokens """
        parts = command.strip().split(" ", 1)
        action = parts[0]
        args = parts[-1] if parts[1:] else None

        tokens = {
            "command": action,
            "args": None,
            "flags": None,
        }

        match action:
            case "add":
                if not args:
                    raise ParseError("'add' expects a string")

                if matches := re.fullmatch(CMD_REGEX['add'], args):
                    tokens["args"] = matches.group(1)
                else:
                    raise ParseError("invalid syntax '%s'" % args)

            case "search":
                if not args:
                    raise ParseError("'search' expects a string")

                if matches := re.fullmatch(CMD_REGEX['search'], args):
                    tokens["args"] = matches.group(1)
                else:
                    raise ParseError("invalid syntax '%s'" % args)

            case "check":
                pass
            case "uncheck":
                pass
            case "delete":
                pass
            case "list":
                pass
            case _:
                raise ParseError("unknown command '%s'" % action)

        return tokens
