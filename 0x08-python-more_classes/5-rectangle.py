#!/usr/bin/python3
"""A module for a rectangle"""


class Rectangle:
  """
  A class representing a rectangle with
  properties for width and height,
  methods for calculating area and
  perimeter, string representations,
  and a custom deletion message.
  """

  def __init__(self, width=0, height=0):
    """
    Initializes a Rectangle object.

    Args:
        width (int, optional): The width of
        the rectangle. Defaults to 0.
        height (int, optional): The height of
        the rectangle. Defaults to 0.
    """
    self._width = width
    self._height = height

  @property
  def width(self):
    """
    Gets the width of the rectangle.

    Returns:
        int: The width of the rectangle.
    """
    return self._width

  @width.setter
  def width(self, value):
    """
    Sets the width of the rectangle.

    Args:
        value (int): The new width.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
    """
    if not isinstance(value, int):
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
    self._width = value

  @property
  def height(self):
    """
    Gets the height of the rectangle.

    Returns:
        int: The height of the rectangle.
    """
    return self._height

  @height.setter
  def height(self, value):
    """
    Sets the height of the rectangle.

    Args:
        value (int): The new height.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
    """
    if not isinstance(value, int):
      raise TypeError("height must be an integer")
    if value < 0:
      raise ValueError("height must be >= 0")
    self._height = value

  def area(self):
    """
    Calculates the area of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return self._width * self._height

  def perimeter(self):
    """
    Calculates the perimeter of the rectangle.

    Returns:
        int: The perimeter of the rectangle
        (0 if width or height is 0).
    """
    if self._width == 0 or self._height == 0:
      return 0
    return 2 * (self._width + self._height)

  def __str__(self):
    """
    Returns a string representation of the
    rectangle using "#".

    Returns:
        str: A string representation of the
        rectangle, or an empty string if
             width or height is 0.
    """
    if self._width == 0 or self._height == 0:
      return ""
    rows = []
    for _ in range(self._height):
      row = "#" * self._width
      rows.append(row)
    return "\n".join(rows)

  def __repr__(self):
    """
    Returns a string representation of the rectangle
    for recreating with eval().

    Returns:
        str: A string representation for eval() to
        create a new Rectangle object.
    """
    return f"Rectangle(width={self._width}, height={self._height})"

  def __del__(self):
    """
    Prints a custom message when a Rectangle
    object is deleted.
    """
    print("Bye rectangle...")
