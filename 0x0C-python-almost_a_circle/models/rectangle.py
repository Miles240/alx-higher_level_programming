#!/usr/bin/python3
"""Contains a Rectangle class"""
from base import Base


class Rectangle(Base):
    """Representation of the Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intiatializing the Rectangle

        Args:
			width (int): the width of the Rectangle
			height (int): the heigth of the Rectangle
			x (int): the x cordinate of the Rectangle
			y (int): the y cordinate of the Rectangle
			id (int): the id of the Rectangle
		"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width of the triangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x coordinate of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y coordinate of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the Rectangle

        Args:
			*args (int): New attributes
				- 1st argument represents the id attribute
				- 2nd argument represents the width attribute
				- 3rd argument represents the height attribute
				- 4th argument represents the x attribute
				- 5th argument represents the y attribute

			**kwargs (int):
				assigns a key/value argument to attributes
        """
        if args and len(args) > 5:
            raise ValueError(
                "update() with *args requires 5 arguments (id, width, height, x, y)"
            )
        attr_list = ["id", "width", "heigth", "x", "y"]
        if args:
            for attr, arg in zip(attr_list, args):
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
