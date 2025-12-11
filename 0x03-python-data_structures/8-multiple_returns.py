#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    first_char = str

    try:
        first_char = sentence[0]
    except Exception:
        first_char = None

    return (length, first_char)
