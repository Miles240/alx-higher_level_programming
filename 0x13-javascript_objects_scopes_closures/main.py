#!/usr/bin/python3
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    # Getter for first_name
    @property
    def first_name(self):
        return self._first_name

    # Setter for first_name
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string")
        self._first_name = value

    # Getter for last_name
    @property
    def last_name(self):
        return self._last_name

    # Setter for last_name
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string")
        self._last_name = value


# Create a Person object
person = Person("John", "Doe")

# Get first_name using the getter
print(person.first_name)  # Output: John

# Set first_name using the setter
person.first_name = "Jane"
print(person.first_name)  # Output: Jane

# Try setting first_name to a non-string value
try:
    person.first_name = 123
except ValueError as e:
    print(e)  # Output: First name must be a string
