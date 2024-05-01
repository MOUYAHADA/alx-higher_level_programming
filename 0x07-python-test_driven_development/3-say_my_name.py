#!/usr/bin/python3
"""This module contains a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """This function prints a name

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
