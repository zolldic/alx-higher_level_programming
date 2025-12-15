#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    new = list(set_1)
    for x in set_2:
        if x in new:
            new.remove(x)
        else:
            new.append(x)
    return set(new)
