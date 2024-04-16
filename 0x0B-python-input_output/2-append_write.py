#!/usr/bin/python3
""" Module for the append_write function """


def append_write(filename="", text=""):
    """ Append a string to a file """
    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
