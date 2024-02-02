class Rectangle:
    """Creating a Triangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intializing the triangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """deleting and calculating the number of instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter for private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private attribute heigth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """String representation of rectangle"""
        string = ""
        string += "\n".join(
            str(self.print_symbol) * self.__width for i in range(self.__height)
        )
        return string

    def __repr__(self):
        """String representation of rectangle"""
        return f"Rectangle ({self.__width}, {self.__height})"
