#!/usr/bin/python3


class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object with first_name, last_name, and age.
        Args:
                first_name (str): students first name
                last_name (str): students last name
                age (int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        If attrs is provided and it's a list of strings, return only the
        attributes listed in attrs. Otherwise, return all attributes.
        """
        if attrs is None:
            # If attrs is None, return all attributes in a dictionary
            return self.__dict__
        else:
            # If attrs is provided and it's a list of strings,
            # return only the attributes listed in attrs

            attribute_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attribute_dict[attr] = getattr(self, attr)
            return attribute_dict
