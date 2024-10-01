#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: the length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property of the length of a side of this square

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of the square.

        Returns:
            Size squared
        """
        return self.__size * self.__size

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
