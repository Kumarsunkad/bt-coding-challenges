# test_solution.py
import unittest
from solution import find_max

class TestFindMax(unittest.TestCase):
    def test_max_normal(self):
        self.assertEqual(find_max([5, 2, 8, 1]), 8)

    def test_max_single(self):
        self.assertEqual(find_max([10]), 10)

if __name__ == "__main__":
    unittest.main()