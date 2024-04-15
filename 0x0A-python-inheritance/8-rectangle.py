#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Method that initializes an instance of class Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
