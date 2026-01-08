# test_solution.py
import unittest
from solution import search_2d

class TestSearch2D(unittest.TestCase):
    def test_found(self):
        matrix = [[1, 2], [3, 4]]
        self.assertTrue(search_2d(matrix, 2))

    def test_not_found(self):
        matrix = [[1, 2], [3, 4]]
        self.assertFalse(search_2d(matrix, 5))

if __name__ == "__main__":
    unittest.main()