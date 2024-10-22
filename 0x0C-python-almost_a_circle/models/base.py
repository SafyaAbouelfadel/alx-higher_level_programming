#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv


Class Base:
    '''A representation of the base of our OOP hierarchy.'''
    __nb_objects = 0
    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''JSONifies a dictionary'''
        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''UnJSONifies a dictionary.'''
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves JSONified object to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unJSONifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as fl:
            return [cls.create(**dct) for dct in cls.from_json_string(fl.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        rect = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as fl:
            reader = csv.reader(fl)
            for row in reader:
                row = [int(rw) for rw in row]
                if cls is Rectangle:
                    dct = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    dct = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                rect.append(cls.create(**dct))
        return rect

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''opens a window and draws all the Rectangles and Squares'''
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for k in list_rectangles + list_squares:
            trt = turtle.Turtle()
            trt.color((randrange(255), randrange(255), randrange(255)))
            trt.pensize(1)
            trt.penup()
            trt.pendown()
            trt.setpos((k.x + trt.pos()[0], k.y - trt.pos()[1]))
            trt.pensize(10)
            trt.forward(k.width)
            trt.left(90)
            trt.forward(k.height)
            trt.left(90)
            trt.forward(k.width)
            trt.left(90)
            trt.forward(k.height)
            trt.left(90)
            trt.end_fill()

        time.sleep(5)
