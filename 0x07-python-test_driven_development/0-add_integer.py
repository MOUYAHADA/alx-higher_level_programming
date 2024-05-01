#!/usr/bin/python3

"""
This module contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers.

    Args:
    (a) is the first integer to add.
    (b) is the second integer to add.

    Returns:
    The sum of a and b.
    """

    if isinstance(a, float) is True:
        a = int(a)
    if isinstance(b, float) is True:
        b = int(b)
    if isinstance(a, int) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False:
        raise TypeError("b must be an integer")
    return a + b
