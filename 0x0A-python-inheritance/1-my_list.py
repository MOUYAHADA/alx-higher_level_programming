#!/usr/bin/python3
""" Module containing MyList class """


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""

        print(sorted(self))
