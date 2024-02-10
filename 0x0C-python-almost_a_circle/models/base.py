#!/usr/bin/python3


class Base:
    """The goal of it is to manage id attribute in all your future
    classes and to avoid duplicating the same cod
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
