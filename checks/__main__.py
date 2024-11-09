""" Entry point for `checks` """

import os
import sys


if __package__ == "":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from checks import cli

if __name__ == "__main__":
    cli.main()
