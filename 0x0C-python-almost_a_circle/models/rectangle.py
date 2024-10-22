#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

           Args:
               width (int): The width of the rectangle.
               height (int): The height of the rectangle.
               x (int, optional): The x-coordinate of the rectangle.
               y (int, optional): The y-coordinate of the rectangle.
               id (int, optional): The identifier for the instance.
                   If None, a unique identifier will be assigned.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of this rectangle

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height of this rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of this rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y of this rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, e=True):
        """Method for validating the value."""
        if not isinstance(value, int): 
            raise TypeError("{} must be an integer".format(name))
        if e and (value < 0):
            raise ValueError("{} must be >= 0".format(name))
        elif not e and (value <= 0):
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Computes area of this rectangle."""
        return self.width * self.height

    def display(self):
        """Prints string representation of this rectangle."""
        t = "\n" * self.y + \
            (" " * self.x + "#" * self.width + "\n") * self.height
        print(t, end="")

    def __str__(self):
        """Returns string info about this rectangle."""
        strg = "[{}] ({}) {}/{} - {}".format(
            str(self.__class__.__name__),
            self.id,
            self.x,
            self.y,
            self.width,
        )
        if type(self) == Rectangle:
            strg += "/{}".format(self.height)
        return strg

    def update(self, *args, **kwargs) -> None:
        """Internal method that updates instance attribute.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args and len(args) != 0:
            c = 0
            for arg in args:
                if c == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif c == 1:
                    self.width = arg
                elif c == 2:
                    self.height = arg
                elif c == 3:
                    self.x = arg
                elif c == 4:
                    self.y = arg
                c += 1
        elif kwargs and len(kwargs) != 0:
            for k, value in kwargs.items():
                if k == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif k in ("width", "height", "x", "y"):
                    setattr(self, k, value) 
    def to_dictionary(self):
        """Returns dictionary representation of this class."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
