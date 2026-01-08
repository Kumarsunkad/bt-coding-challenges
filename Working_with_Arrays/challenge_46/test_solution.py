# test_solution.py
import unittest
from solution import sum_elements

class TestSumElements(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(sum_elements([1, 2, 3]), 6)

    def test_sum_empty(self):
        self.assertEqual(sum_elements([]), 0)

if __name__ == "__main__":
    unittest.main()