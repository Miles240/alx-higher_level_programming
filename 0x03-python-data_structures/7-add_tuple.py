#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    # Perform element-wise addition and return a new tuple
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result_tuple
