#!/usr/bin/python3
"""Contains a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a json string to a new file"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
