#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for key, value in copy.items():
        copy.update({key: value * 2})
    return copy

