#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for idx, val in enumerate(x):
            if idx == len(x) - 1:
                sep = ''
            else:
                sep = ' '
            print('{:d}{}'.format(val, sep), end='')
        print()
