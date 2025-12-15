# test_solution.py
import unittest
from solution import calculate_discount

class TestDiscountCalculation(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(calculate_discount(1000, 10), 900)
        self.assertEqual(calculate_discount(1500, 20), 1200)
    
    def test_zero_discount(self):
        self.assertEqual(calculate_discount(500, 0), 500)
    
    def test_zero_total_amount(self):
        self.assertEqual(calculate_discount(0, 10), 0)
    
    def test_float_values(self):
        self.assertAlmostEqual(calculate_discount(1234.56, 15.5), 1042.3532, places=4)

if __name__ == "__main__":
    unittest.main()
