#!/usr/bin/python3
"""Module for the Square class"""


class Square:
    """Create a square instance"""

    def __init__(self, size=0):
        """Create new square"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
