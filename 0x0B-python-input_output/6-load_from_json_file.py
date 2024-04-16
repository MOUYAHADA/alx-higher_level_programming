#!/usr/bin/python3
""" Module for the load_from_json_file function """
import json


def load_from_json_file(filename):
    """ Load object from a json file """
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.loads(f.read())
