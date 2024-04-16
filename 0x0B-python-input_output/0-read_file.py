#!/usr/bin/python3
""" Module for the read_file function """


def read_file(filename=""):
    """ Reads a text file and prints it to stdout """
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end="")
