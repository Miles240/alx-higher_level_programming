#!/usr/bin/python3
"""Contains a read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to Stdout"""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
