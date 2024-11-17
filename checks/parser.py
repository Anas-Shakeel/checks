""" Contains a parser that parses specific commands """

import re
from checks.exceptions import ParseError

CMD_REGEX = {
    "string": re.compile(r"\"(.+)\""),
    "id": re.compile(r"\d+"),
    "check_flag": re.compile(r"-a|--all"),
    "uncheck_flag": re.compile(r"-a|--all"),
    "remove_flag": re.compile(r"-a|--all"),
    "list": re.compile(r"(?:-c|--completed)|(?:-p|--pending)|(?:-m|--minimal)"),
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
            "action": action,
            "args": [],
            "flags": [],
        }

        match action:
            case "add" | "a":
                if not args:
                    raise ParseError("'add' expects a string")

                for part in args.split(","):
                    part = part.strip()
                    if matches := re.fullmatch(CMD_REGEX['string'], part):
                        tokens["args"].append(matches.group(1))
                    else:
                        raise ParseError("invalid syntax '%s'" % part)

            case "search" | "s":
                if not args:
                    raise ParseError("'search' expects a string")

                if matches := re.fullmatch(CMD_REGEX['string'], args):
                    tokens["args"].append(matches.group(1))
                else:
                    raise ParseError("invalid syntax '%s'" % args)

            case "check" | "c":
                if not args:
                    raise ParseError("'check' expects an id")

                for part in args.split(","):
                    part = part.strip()

                    if re.fullmatch(CMD_REGEX['id'], part):
                        tokens["args"].append(int(part))
                    elif re.fullmatch(CMD_REGEX['check_flag'], part):
                        tokens['flags'].append(part)
                    else:
                        raise ParseError("invalid syntax '%s'" % part)

            case "uncheck" | "uc":
                if not args:
                    raise ParseError("'uncheck' expects an id")

                for part in args.split(","):
                    part = part.strip()

                    if re.fullmatch(CMD_REGEX['id'], part):
                        tokens["args"].append(int(part))
                    elif re.fullmatch(CMD_REGEX['uncheck_flag'], part):
                        tokens['flags'].append(part)
                    else:
                        raise ParseError("invalid syntax '%s'" % part)

            case "remove" | "rm":
                if not args:
                    raise ParseError("'remove' expects an id")

                for part in args.split(","):
                    part = part.strip()

                    if re.fullmatch(CMD_REGEX['id'], part):
                        tokens["args"].append(int(part))
                    elif re.fullmatch(CMD_REGEX['remove_flag'], part):
                        tokens['flags'].append(part)
                    else:
                        raise ParseError("invalid syntax '%s'" % part)

            case "list" | "ls":
                if args:
                    for part in args.split(" "):
                        if matches := re.fullmatch(CMD_REGEX['list'], part):
                            if part not in tokens['flags']:
                                tokens['flags'].append(part)
                        else:
                            raise ParseError("invalid syntax '%s'" % part)

            case "help" | "h":
                if args:
                    raise ParseError("invalid syntax '%s'" % args)

            case "quit" | "q":
                if args:
                    raise ParseError("invalid syntax '%s'" % args)

            case "save" | "sv":
                if args:
                    raise ParseError("invalid syntax '%s'" % args)

            case "clear" | "cls":
                if args:
                    raise ParseError("invalid syntax '%s'" % args)

            case _:
                raise ParseError("unknown command '%s'" % action)

        return tokens
