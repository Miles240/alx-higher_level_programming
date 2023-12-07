#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = dict()

    for m, n in a_dictionary.items():
        new_dict[m] = n * 2
    return new_dict
