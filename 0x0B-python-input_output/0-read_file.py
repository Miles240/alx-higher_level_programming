#!/usr/bin/python3


def read_file(filename=""):
    """Reads a text file and prints it to Stdout"""

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line)
