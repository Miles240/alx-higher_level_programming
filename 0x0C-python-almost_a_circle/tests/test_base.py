#!/usr/bin/python3
"""Test file for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Bass class"""

    def test_init(self):
        """Tests cases for the __init__ method"""
        # test if the id is not provided
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, base_2.id - 1)

        obj2 = Base(10)
        self.assertEqual(obj2.id, 10)

        # test if the id == None
        obj3 = Base(None)
        self.assertEqual(obj3.id, 3)

    def test_to_json_string(self):
        """Tests cases for to_json_string method"""

        # test the conversion of list of dictionaries to JSON string
        list_dict = [{"name":"miles"},{"name":"bertina"},{"name":"essam"}]
        json_string = Base.to_json_string(list_dict)
        expected_string = '[{"name": "miles"}, {"name": "bertina"}, {"name": "essam"}]'
        self.assertEqual(json_string, expected_string)

        # test the conversion of an empty list to JSON string
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        self.assertEqual(json_string, "[]")

        # test the conversion of None to JSON string
        none_list = None
        json_string = Base.to_json_string(none_list)
        self.assertEqual(json_string, "[]")

        def test_save_to_file(self):
            """Test the save_to_file class method"""

            # Test saving list of objects to file
            class Dummy:
                def __init__(self, id, name):
                    self.id = id
                    self.name = name

                def to_dictionary(self):
                    return {"id": self.id, "name": self.name}

            obj1 = Dummy(1, "Alice")
            obj2 = Dummy(2, "Bob")
            list_objs = [obj1, obj2]

            Base.save_to_file(list_objs)

            # Read from file and verify content
            with open("Dummy.json", "r") as file:
                data = file.read()
                expected_data = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
                self.assertEqual(data, expected_data)

            # Test saving empty list to file
            Base.save_to_file([])
            with open("Base.json", "r") as file:
                data = file.read()
                self.assertEqual(data, "[]")

            # Test saving None to file
            Base.save_to_file(None)
            with open("Base.json", "r") as file:
                data = file.read()
                self.assertEqual(data, "[]")


if __name__ == "__main__":
    unittest.main()
