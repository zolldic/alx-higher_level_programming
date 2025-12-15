#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new = []
    try:
        for x in range(list_length):
            try:
                new.append(my_list_1[x] / my_list_2[x])
            except ZeroDivisionError:
                print("division by 0")
                new.append(0)
            except TypeError:
                print("worng type")
                new.append(0)
            except IndexError:
                print("out of range")
    finally:
        return new
