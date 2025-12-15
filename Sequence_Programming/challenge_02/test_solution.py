# test_solution.py
import unittest
from solution import calculate_simple_interest

class TestSimpleInterest(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(calculate_simple_interest(1000, 5, 2), 100)
        self.assertEqual(calculate_simple_interest(5000, 3, 4), 600)
    
    def test_zero_values(self):
        self.assertEqual(calculate_simple_interest(0, 5, 2), 0)
        self.assertEqual(calculate_simple_interest(1000, 0, 2), 0)
        self.assertEqual(calculate_simple_interest(1000, 5, 0), 0)
    
    def test_float_values(self):
        self.assertAlmostEqual(calculate_simple_interest(1500.50, 4.5, 3.2), 216.072)

if __name__ == "__main__":
    unittest.main()
