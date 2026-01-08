# test_solution.py
import unittest
from solution import reverse_array

class TestReverseArray(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_array([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_reverse_single(self):
        self.assertEqual(reverse_array([5]), [5])

if __name__ == "__main__":
    unittest.main()