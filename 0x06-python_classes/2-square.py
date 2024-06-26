#!/usr/bin/python3
"""Module for the Square class"""


class Square:
    """Create a square instance"""

    def __init__(self, size=0):
        """Create new square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

    self.__size = size
