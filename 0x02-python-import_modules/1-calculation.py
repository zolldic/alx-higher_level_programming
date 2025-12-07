#!/usr/bin/python3

functions = __import__("calculator_1")

a = 10
b = 5

if __name__ == '__main__':
    print("{} + {} = {}".format(a, b, functions.add(a, b)))
    print("{} - {} = {}".format(a, b, functions.sub(a, b)))
    print("{} * {} = {}".format(a, b, functions.mul(a, b)))
    print("{} / {} = {}".format(a, b, functions.div(a, b)))
