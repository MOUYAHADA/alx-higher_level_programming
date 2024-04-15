#!/usr/bin/python3
""" Module for the BaseGeometry class """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Calculate area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integer """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
