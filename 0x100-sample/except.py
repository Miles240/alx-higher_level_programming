#!/usr/bin/python3
"""
Script to save and load files
"""
from sys import argv
from os import path
save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
load_from_json_file = _import_('6-load_from_json_file').load_from_json_file


file = "add_item.json"

if path.exists(file):
    my_list = load_from_json_file(file)
else:
    my_list = []

if len(argv) > 1:
    for i in range(1, len(argv)):
        my_list.append(argv[i])

save_to_json_file(my_list, file)