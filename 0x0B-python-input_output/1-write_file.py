#!/usr/bin/python3
"""Contains a write_file function"""


def write_file(filename="", text=""):
    """Creates/Write in a file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(str(text))
