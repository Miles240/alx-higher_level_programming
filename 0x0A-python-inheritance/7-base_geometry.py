#!/usr/bin/python3
class BaseGeometry:
    """Class for base geometry"""
    def area(self):
        """Area of base geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validator for integer"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

