#!/usr/bin/python3

"""Adds all argument to a new json file"""

import os.path
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

if not os.path.isfile(filename):
    json_data = []
else:
    json_data = load_from_json_file(filename)

for arg in argv[1:]:
    json_data.append(arg)
save_to_json_file(json_data, filename)
