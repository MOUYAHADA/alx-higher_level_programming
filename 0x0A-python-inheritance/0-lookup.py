#!/usr/bin/python3
"""Module for the lookup functionwhich returns
a list of available attributes and methods of an object"""


def lookup(obj):
    """Returns a list of available attributes & methods of an object"""
    return dir(obj)
