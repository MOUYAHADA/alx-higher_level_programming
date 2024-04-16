#!/usr/bin/python3
""" Module for the save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """ Save an object as json to a file """
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
