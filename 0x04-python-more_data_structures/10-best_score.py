#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
