#!/usr/bin/python3

"""Adds all argument to a new json file"""

import os.path
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"

if not os.path.isfile(file_name):
    json_data = []
else:
    json_data = load_from_json_file(file_name)

if len(argv) > 1:
    for arg in range(1, len(argv)):
        json_data.append(argv[arg])
save_to_json_file(json_data, file_name)
