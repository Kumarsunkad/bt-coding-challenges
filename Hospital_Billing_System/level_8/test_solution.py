# test_solution.py
import unittest
from solution import apply_discounts

class TestApplyDiscounts(unittest.TestCase):
    def test_senior_discount(self):
        discounted, disc = apply_discounts(2000, 65)
        self.assertAlmostEqual(discounted, 1800)
        self.assertAlmostEqual(disc, 200)

    def test_high_bill_discount(self):
        discounted, disc = apply_discounts(6000, 30)
        self.assertAlmostEqual(discounted, 5700)
        self.assertAlmostEqual(disc, 300)

    def test_both_discounts(self):
        discounted, disc = apply_discounts(6000, 65)
        expected_disc = 6000 * 0.10 + 6000 * 0.05
        self.assertAlmostEqual(discounted, 6000 - expected_disc)
        self.assertAlmostEqual(disc, expected_disc)

if __name__ == "__main__":
    unittest.main()