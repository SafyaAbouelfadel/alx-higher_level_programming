#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializatin of a new square
        Args:
            size (int): Size of the new square
            position (int, int): Position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print("")
            return

         [print("") for k in range(0, self.__position[1])]
        for k in range(0, self.__size):
            [print(" ", end="") for c in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for k in range(0, self.__position[1])]
        for k in range(0, self.__size):
            [print(" ", end="") for c in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
