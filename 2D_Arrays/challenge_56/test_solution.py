# test_solution.py
import unittest
from solution import sum_2d

class TestSum2D(unittest.TestCase):
    def test_sum(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(sum_2d(matrix), 10)

    def test_empty(self):
        self.assertEqual(sum_2d([]), 0)

if __name__ == "__main__":
    unittest.main()