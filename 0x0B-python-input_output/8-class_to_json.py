#!/usr/bin/python3
""" Mocule for the class_to_json function """


def class_to_json(obj):
    """ Function that returns the json representation of a class """
    return obj.__dict__
