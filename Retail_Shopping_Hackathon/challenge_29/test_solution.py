# test_solution.py
import unittest
from solution import calculate_tax

class TestTaxCalculation(unittest.TestCase):
    def test_low_tax(self):
        total, tax = calculate_tax(4000)
        self.assertEqual(total, 4200)
        self.assertEqual(tax, 200)

    def test_mid_tax(self):
        total, tax = calculate_tax(10000)
        self.assertEqual(total, 11000)
        self.assertEqual(tax, 1000)

    def test_high_tax(self):
        total, tax = calculate_tax(25000)
        self.assertEqual(total, 28750)
        self.assertEqual(tax, 3750)

if __name__ == "__main__":
    unittest.main()