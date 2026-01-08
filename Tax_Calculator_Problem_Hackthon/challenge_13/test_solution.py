# test_solution.py
import unittest
from solution import calculate_tax

class TestTaxCalculation(unittest.TestCase):
    def test_no_tax(self):
        total, base, cess = calculate_tax(300000)
        self.assertEqual(total, 0)
        self.assertEqual(base, 0)
        self.assertEqual(cess, 0)

    def test_rebate(self):
        total, base, cess = calculate_tax(700000)
        self.assertEqual(total, 0)

    def test_with_tax(self):
        total, base, cess = calculate_tax(1000000)
        expected_base = 300000 * 0.05 + 300000 * 0.10 + 100000 * 0.15
        expected_cess = expected_base * 0.04
        self.assertAlmostEqual(base, expected_base)
        self.assertAlmostEqual(cess, expected_cess)
        self.assertAlmostEqual(total, expected_base + expected_cess)

if __name__ == "__main__":
    unittest.main()