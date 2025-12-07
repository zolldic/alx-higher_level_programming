#!/usr/bin/python3
import sys


def printArgs():
    lst = []

    length = len(sys.argv) - 1
    lst.append(length)
    if length == 1:
        lst.append("argument:")
    else:
        if length == 0:
            lst.append("arguments.")
        else:
            lst.append("arguments:")

    for idx, value in enumerate(sys.argv):
        if idx > 0:
            lst.append(value)

    print("{} {}".format(lst[0], lst[1]))
    for idx in range(lst[0]):
        print("{}: {}".format(idx + 1, lst[idx + 2]))


if __name__ == '__main__':
    printArgs()
