#!/usr/bin/python3
"""
This module define a class (Square)
"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: if the self.__size is not integer
            ValueError: if self.__size is less than zero
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
