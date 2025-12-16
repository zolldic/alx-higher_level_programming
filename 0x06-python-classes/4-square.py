#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
