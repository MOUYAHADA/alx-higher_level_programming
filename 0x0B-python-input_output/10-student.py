#!/usr/bin/python3
""" Module for the student class """


class Student:
    """ Returns the dictionary representation of a Student instance"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
