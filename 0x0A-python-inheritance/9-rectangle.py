#!/usr/bin/python3
""" Module for the Rectangle class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Creates new rectangle """
        self.__height = height
        self.__width = width
        self.integer_validator(self.__height)
        self.integer_validator(self.__width)

    def area(self):
        """ Calculate self """
        return self.__width * self.__height

    def __str__(self):
        """ String representation of rectangle """
        return f"[Rectangle] {width}/{height}"
