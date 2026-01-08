# test_solution.py
import unittest
from solution import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))

    def test_not_found(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))

    def test_empty(self):
        self.assertFalse(binary_search([], 1))

if __name__ == "__main__":
    unittest.main()