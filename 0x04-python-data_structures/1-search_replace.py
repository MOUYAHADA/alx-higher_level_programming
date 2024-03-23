#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replace an element by another in a new list."""
    return [replace if x == search else x for x in my_list]
