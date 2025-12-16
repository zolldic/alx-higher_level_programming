#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
            position tuple(int, int): The position of the new square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position of the square

        Returns:
            tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: if position is not a tuple with two integer.
        """

        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Print hash symbol (#) based on the size of the area.
        """

        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end='')
            for _ in range(self.__size):
                print("#", end='')
            print()
