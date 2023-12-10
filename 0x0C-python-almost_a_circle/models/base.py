#!/usr/python3

""" Document the module """


class Base():
    """ Document the class """

    __nb_objects = 0

    def __init__(self, id=None):
        """Document the function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
