#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    if not my_list:
        return None

    for num in my_list:
        new_list.append(num % 2 == 0)
    return new_list
