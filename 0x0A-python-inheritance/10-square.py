#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size):
        """Method that initializes an instance of class Square"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method that returns the area of the square"""
        return self.__size**2
