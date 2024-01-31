from turtle import width


class Rectangle:
    def __init__(self, width=0, heigth=0):
        self.width = width
        self.heigth = heigth

    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if isinstance(int(value)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if isinstance(int(value)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height
    
    def parameter(self):
        
