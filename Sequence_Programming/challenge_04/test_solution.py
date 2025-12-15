# test_solution.py
import unittest
from solution import swap_numbers

class TestSwapNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(swap_numbers(5, 10), (10, 5))
        self.assertEqual(swap_numbers(20, 30), (30, 20))
    
    def test_negative_numbers(self):
        self.assertEqual(swap_numbers(-3, 7), (7, -3))
        self.assertEqual(swap_numbers(-5, -10), (-10, -5))
    
    def test_zero_and_positive(self):
        self.assertEqual(swap_numbers(0, 15), (15, 0))

if __name__ == "__main__":
    unittest.main()
