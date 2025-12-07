#!/usr/bin/python3

sep = ", "
for x in range(0, 10):
    if x == 9:
        print()
    for y in range(x, 10):
        if x != y:
            if x == 8:
                sep = ""
            print("{}{}{}".format(x, y, sep), end="")
