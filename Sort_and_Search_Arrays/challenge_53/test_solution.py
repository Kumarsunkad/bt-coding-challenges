# test_solution.py
import unittest
from solution import sort_array

class TestSortArray(unittest.TestCase):
    def test_ascending(self):
        self.assertEqual(sort_array([3, 1, 4, 2], 'ascending'), [1, 2, 3, 4])

    def test_descending(self):
        self.assertEqual(sort_array([3, 1, 4, 2], 'descending'), [4, 3, 2, 1])

    def test_invalid(self):
        self.assertEqual(sort_array([3, 1, 4, 2], 'invalid'), [3, 1, 4, 2])

if __name__ == "__main__":
    unittest.main()