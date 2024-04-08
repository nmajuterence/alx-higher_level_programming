#!/usr/bin/python3
"""Define a class square"""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

