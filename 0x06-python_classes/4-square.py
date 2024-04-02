#!/usr/bin/python3
"""Module for the square class"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Create new square"""

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value
