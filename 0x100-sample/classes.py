class Square:
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._value = value
        if not int(self._value):
            raise TypeError("size must be an integer")
        elif self._value < 0:
            raise ValueError("size must be >= 0")

    def __init(self, size = 0):
        self.size = size

    def area(self):
        return self._size  ** 2
