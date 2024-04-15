#!/usr/bin/python3
""" Module for MyInt class """


class MyInt(int):
    """ MyInt class """
    def __eq__(self, other):
        """ Equals """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ Unequal """
        return not super().__ne__(other)
