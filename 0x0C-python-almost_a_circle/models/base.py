#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv
import turtle


class Base:
    """A representation of the base of our OOP hierarchy.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initialize a Base instance.

        Args:
            id (int, optional): The identifier for the instance.
                If None, a unique identifier will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.
        """
        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string) -> list:
        """UnJSONifies a dictionary.

        Args:
            json_string (str): JSON-formatted string.
        """
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSONified object to file.

        Args:
            list_objs (list): List of objects to save.
        """
        fl = cls.__name__ + ".json"
        with open(fl, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance based on a dictionary.

        Args:
            **dictionary (dict): Dictionary containing object attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Loads string from file and unJSONifies."""
        fl = cls.__name__ + ".json"
        try:
            with open(fl) as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves object to csv file.

        Args:
            list_objs (list): List of objects to save.
        """
        fl = cls.__name__ + ".csv"
        with open(fl, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldname)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a CSV file."""
        fl = cls.__name__ + ".csv"
        try:
            with open(fl, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                list_dcts = csv.DictReader(f, fieldnames=fieldname)
                list_dcts = [
                    dict([key, int(value)] for key, value in d.items())
                    for d in list_dcts
                ]
                return [cls.create(**obj) for obj in list_dcts]
        except IOError:
            return [] 

    @staticmethod
    def draw(list_rectangles, list_squares) -> None:
        """Draw rectangles and squares using the turtle graphics library.

        Args:
            list_rectangles (list): List of rectangles to draw.
            list_squares (list): List of squares to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#a6a6a6")
        turt.pensize(2)
        turt.shape("turtle")

        turt.color("#af0000")
        for rect in list_rectangles:
            turt.penup()
            turt.goto(rect.x, rect.y)
            turt.pendown()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)

        turt.color("#0d47cc")
        for sqr in list_squares:
            turt.penup()
            turt.goto(sqr.x, sqr.y)
            turt.pendown()
            for _ in range(4):
                turt.forward(sqr.width)
                turt.left(90)

        turtle.exitonclick()
