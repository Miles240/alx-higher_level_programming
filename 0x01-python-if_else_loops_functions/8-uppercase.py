#!/usr/bin/python3


def uppercase(str):
    result = ""
    for char in str:
        if "a" <= char <= "z":
            uppercase_char = chr(ord(char) - ord("a") + ord("A"))
            result += uppercase_char
        else:
            result += char
    return result
