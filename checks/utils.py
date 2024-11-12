""" Contains functions that don't fit elsewhere """

from datetime import datetime

# Datetime format used across project
DATE_FORMAT: str = "%d-%m-%Y %H:%M:%S"


def get_current_datetime():
    """ Returns the current datetime """
    return datetime.now().strftime(DATE_FORMAT)
