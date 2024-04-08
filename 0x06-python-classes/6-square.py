#!/usr/bin/python3
"""Define a class square"""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or position contains non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If value contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value) or any(num < 0 for num in value):
            raise ValueError("position must contain positive integers only")

        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
