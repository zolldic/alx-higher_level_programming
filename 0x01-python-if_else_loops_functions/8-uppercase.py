#!/usr/bin/python3


def uppercase(str):
    new = []
    for letter in str:
        if ord(letter) <= 122 and ord(letter) >= 97:
            new.append(chr(ord(letter) - 32))
        else:
            new.append(letter)
    print("{}".format("".join(new)))
