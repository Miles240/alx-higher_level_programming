#!/usr/bin/python3

"""Contains a append_write function"""


def append_write(filename="", test=""):
    """Create/Appends a string to a file"""

    with open(filename, "a", encoding="utf-8") as file:
        return str(file.write(test))
