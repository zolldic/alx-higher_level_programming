#!/usr/bin/python3


def printNumbers():
    sum = 0

    for key, value in enumerate(sys.argv):
        if key > 0:
            sum += int(value)

    print(sum)


if __name__ == '__main__':
    import sys
    printNumbers()
