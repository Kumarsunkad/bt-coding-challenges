# test_solution.py
import unittest
from solution import find_min

class TestFindMin(unittest.TestCase):
    def test_min_normal(self):
        self.assertEqual(find_min([5, 2, 8, 1]), 1)

    def test_min_single(self):
        self.assertEqual(find_min([10]), 10)

if __name__ == "__main__":
    unittest.main()