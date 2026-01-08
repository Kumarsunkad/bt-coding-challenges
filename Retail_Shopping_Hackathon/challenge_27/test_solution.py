# test_solution.py
import unittest
from solution import apply_discounts

class TestDiscounts(unittest.TestCase):
    def test_no_discount(self):
        total, disc = apply_discounts(5000, 10)
        self.assertEqual(total, 5000)
        self.assertEqual(disc, 0)

    def test_amount_discount(self):
        total, disc = apply_discounts(12000, 10)
        self.assertEqual(total, 10800)
        self.assertEqual(disc, 1200)

    def test_quantity_discount(self):
        total, disc = apply_discounts(5000, 25)
        self.assertEqual(total, 4750)
        self.assertEqual(disc, 250)

    def test_both_discounts(self):
        total, disc = apply_discounts(12000, 25)
        expected_disc = 12000 * 0.10 + 12000 * 0.05
        self.assertAlmostEqual(total, 12000 - expected_disc)
        self.assertAlmostEqual(disc, expected_disc)

if __name__ == "__main__":
    unittest.main()