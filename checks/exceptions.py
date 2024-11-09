""" Contains all custom exceptions used in this project """


class ParseError(Exception):
    """ exception for command parse errors """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.args = args