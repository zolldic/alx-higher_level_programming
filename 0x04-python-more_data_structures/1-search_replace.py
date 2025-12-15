#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new = my_list.copy()

    for idx, val in enumerate(new):
        if val == search:
            new[idx] = replace
    return new
