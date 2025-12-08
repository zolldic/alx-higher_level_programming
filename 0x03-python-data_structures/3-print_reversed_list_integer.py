#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    res = my_list[::-1]
    for idx in res:
        print("{:d}".format(idx))
