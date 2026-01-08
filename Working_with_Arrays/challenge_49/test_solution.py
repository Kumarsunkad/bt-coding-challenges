# test_solution.py
import unittest
from solution import search_element

class TestSearchElement(unittest.TestCase):
    def test_found(self):
        self.assertTrue(search_element([5, 2, 8, 1], 2))

    def test_not_found(self):
        self.assertFalse(search_element([5, 2, 8, 1], 3))

if __name__ == "__main__":
    unittest.main()