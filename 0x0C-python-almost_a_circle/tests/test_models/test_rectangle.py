#!/usr/bin/python3

"""Test file for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_init(self):
        """test cases for __init__ method"""

        # test with all values provided
        rect_1 = Rectangle(10, 10, 6, 4, 3)
        self.assertEqual(rect_1.width, 10)
        self.assertEqual(rect_1.height, 10)
        self.assertEqual(rect_1.x, 6)
        self.assertEqual(rect_1.y, 4)
        self.assertEqual(rect_1.id, 3)

        # test conversion with values in provided in float
        rect_2 = Rectangle(5.3, 8.4, 2.2, 6.0, 3)
        self.assertEqual(rect_2.width, 5)
        self.assertEqual(rect_2.height, 8)
        self.assertEqual(rect_2.x, 2)
        self.assertEqual(rect_2.y, 6)
        self.assertIsNotNone(rect_2.id)

        # test with only width and height provided
        rect_3 = Rectangle(5, 9)
        self.assertEqual(rect_3.width, 5)
        self.assertEqual(rect_3.height, 9)
        self.assertEqual(rect_3.x, 0)
        self.assertEqual(rect_3.y, 0)
        self.assertIsNotNone(rect_3.id)

        # Test initialization with invalid arguments
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10)
        with self.assertRaises(ValueError):
            Rectangle(0, 10)
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid")
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_area(self):
        """test cases for the area method"""
        area_1 = Rectangle.area(5, 5)
        self.assertEqual(area_1, 25)

    def test_display(self):
        """test case for display method"""
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        """test cases for update method"""
        rect = Rectangle(5, 10)
        rect.update(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

        rect.update(id=10, x=20)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 20)
        self.assertEqual(rect.y, 5)

    def test_str(self):
        """Test the __str__ method"""
        rect = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (3) 1/2 - 5/10")
