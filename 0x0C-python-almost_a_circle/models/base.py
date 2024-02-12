#!/usr/bin/python3
"""Base class"""
import json


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

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open("filename", "w") as file:
            if list_objs == None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(json.dump(list_dicts))
