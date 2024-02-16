#!/usr/bin/python3
"""Contains a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Intiatializing the Square

        Args:
                size (int): the width/height of the Square
                x (int): the x cordinate of the Square
                y (int): the y cordinate of the Square
                id (int): the id of the Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the attribute size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square

        Args:
                *args (int): New attributes
                  - 1st argument represents the id attribute
                  - 2nd argument represents the width/height attribute
                  - 3rd argument represents the x attribute
                  - 4th argument represents the y attribute

                **kwargs (int):
                        assigns a key/value argument to attributes
        """
        attr_list = ["id", "size", "x", "y"]
        if args:
            for attr, arg in zip(attr_list, args):
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.size}"
