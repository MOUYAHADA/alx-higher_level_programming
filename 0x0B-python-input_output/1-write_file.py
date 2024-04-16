#!/usr/bin/python3
""" Module for the write_file function """


def write_file(filename="", text=""):
    """ Writes a string to a file """
    with open(filename, mode="w") as f:
        return f.write(text)
