#!/usr/bin/python3
"""Test file for the Square class"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_init(self):
        """Test the __init__ method"""
        # Test initialization with all arguments provided
        square1 = Square(5, 1, 2, 3)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.width, 5)
        self.assertEqual(square1.height, 5)
        self.assertEqual(square1.x, 1)
        self.assertEqual(square1.y, 2)
        self.assertEqual(square1.id, 3)

        # Test initialization with default values
        square2 = Square(7)
        self.assertEqual(square2.size, 7)
        self.assertEqual(square2.width, 7)
        self.assertEqual(square2.height, 7)
        self.assertEqual(square2.x, 0)
        self.assertEqual(square2.y, 0)
        self.assertIsNotNone(square2.id)

        # Test initialization with only size provided
        square3 = Square(3)
        self.assertEqual(square3.size, 3)
        self.assertEqual(square3.width, 3)
        self.assertEqual(square3.height, 3)
        self.assertEqual(square3.x, 0)
        self.assertEqual(square3.y, 0)
        self.assertIsNotNone(square3.id)

    def test_update(self):
        """Test the update method"""
        square = Square(5, 1, 2, 3)
        square.update(10, 8, 9, 7)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 9)
        self.assertEqual(square.y, 7)

        square.update(id=20, x=30)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 7)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        square = Square(5, 1, 2, 3)
        dictionary = square.to_dictionary()
        expected_dict = {"id": 3, "size": 5, "x": 1, "y": 2}
        self.assertEqual(dictionary, expected_dict)

    def test_str(self):
        """Test the __str__ method"""
        square = Square(5, 1, 2, 3)
        self.assertEqual(str(square), "[square] (3) 1/2 - 5")


if __name__ == "__main__":
    unittest.main()
