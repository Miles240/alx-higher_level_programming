#!/usr/bin/python3
"""Contains a from_json_string function"""

import json


def from_json_string(my_str):
    """Converts a json string to a python dict"""
    return json.loads(my_str)
