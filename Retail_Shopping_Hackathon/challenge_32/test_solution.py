# test_solution.py
import unittest
from solution import check_minimum_purchase

class TestMinimumPurchase(unittest.TestCase):
    def test_above_minimum(self):
        self.assertTrue(check_minimum_purchase(600))

    def test_below_minimum(self):
        self.assertFalse(check_minimum_purchase(400))

    def test_exact_minimum(self):
        self.assertTrue(check_minimum_purchase(500))

if __name__ == "__main__":
    unittest.main()