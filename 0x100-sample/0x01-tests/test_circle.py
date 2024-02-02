import unittest
from circle import calc


class TestCircleArea(unittest.TestCase):
    def test_areas(self):
        result = calc(2, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
