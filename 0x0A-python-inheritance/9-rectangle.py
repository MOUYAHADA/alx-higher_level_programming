#!/usr/bin/python3
""" Module for the Rectangle class """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Creates new rectangle """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ Calculate self """
        return self.__width * self.__height

    def __str__(self):
        """ String representation of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
