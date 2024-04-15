#!/usr/bin/python3
""" Module for the Rectangle class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Creates new rectangle """
        BaseGeometry.integer_validator(height)
        BaseGeometry.integer_validator(width)
        self.__height = height
        self.__width = width
