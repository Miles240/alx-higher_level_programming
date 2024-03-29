#!/usr/bin/python3
"""Contains a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a json string in a new file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
