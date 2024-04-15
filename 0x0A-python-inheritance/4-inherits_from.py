#!/usr/bin/python3
""" Module for the inherits from function """


def inherits_from(obj, a_class):
    """ Checks if object is instance of a subclass of a specified class"""
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
