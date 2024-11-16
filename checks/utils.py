""" Contains functions that don't fit elsewhere """

from datetime import datetime
from checks.pinsy import Pins
from checks.pinsy.utils import clear_terminal


# Pins Instance to use across project
pins = Pins(color_mode=8)

# Datetime format used across project
DATE_FORMAT: str = "%d-%m-%Y %H:%M:%S"


def get_current_datetime():
    """ Returns the current datetime """
    return datetime.now().strftime(DATE_FORMAT)


def err(err_type, err_msg):
    """ Prints the `error` message. (USE ONLY FOR INTERNAL CHECKS ERRORS) """
    print(pins.create_status(err_type, err_msg, label_fg="light_red", text_fg="light_red"))
