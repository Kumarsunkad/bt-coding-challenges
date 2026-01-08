# test_solution.py
import unittest
from solution import count_odd_even

class TestCountOddEven(unittest.TestCase):
    def test_mixed(self):
        odd, even = count_odd_even([1, 2, 3, 4, 5])
        self.assertEqual(odd, 3)
        self.assertEqual(even, 2)

    def test_all_even(self):
        odd, even = count_odd_even([2, 4, 6])
        self.assertEqual(odd, 0)
        self.assertEqual(even, 3)

if __name__ == "__main__":
    unittest.main()