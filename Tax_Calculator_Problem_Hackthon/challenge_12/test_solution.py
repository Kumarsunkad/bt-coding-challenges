# test_solution.py
import unittest
from solution import calculate_taxable_income

class TestTaxableIncome(unittest.TestCase):
    def test_above_deduction(self):
        self.assertEqual(calculate_taxable_income(600000), 550000)

    def test_below_deduction(self):
        self.assertEqual(calculate_taxable_income(40000), 0)

    def test_exact_deduction(self):
        self.assertEqual(calculate_taxable_income(50000), 0)

if __name__ == "__main__":
    unittest.main()