#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
            y (int, optional): The y-coordinate of the square.
            id (int, optional): The identifier for the instance.
                If None, a unique identifier will be assigned.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about this square"""

        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self) -> int:
        """Size of this square."""
        return self.width

    @size.setter
    def size(self, value) -> None:
        """Set the size of the square.

        Args:
            value (int): The size value to set.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args and len(args) != 0:
            c = 0
            for arg in args:
                if c == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif c == 1:
                    self.size = arg
                elif c == 2:
                    self.x = arg
                elif c == 3:
                    self.y = arg
                c += 1
        elif kwargs and len(kwargs) != 0:
            for k, value in kwargs.items():
                if k == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif k in ("size", "x", "y"):
                    setattr(self, k, value)

    def to_dictionary(self):
        """Returns dictionary representation of this class."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
