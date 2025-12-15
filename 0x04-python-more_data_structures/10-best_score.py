#!/usr/bin/python3

def best_score(a_dictionary):
    biggest = 0
    k = str()

    if not a_dictionary:
        return None

    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            k = key

    return k
