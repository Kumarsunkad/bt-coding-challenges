# test_solution.py
import unittest
from solution import apply_promo_discount

class TestPromoDiscount(unittest.TestCase):
    def test_promo_applied(self):
        items = [{'code': 'PROMO10', 'quantity': 1, 'price': 100}]
        apply_promo_discount(items)
        self.assertEqual(items[0]['total'], 90)

    def test_no_promo(self):
        items = [{'code': 'A1', 'quantity': 2, 'price': 50}]
        apply_promo_discount(items)
        self.assertEqual(items[0]['total'], 100)

    def test_mixed(self):
        items = [
            {'code': 'A1', 'quantity': 2, 'price': 50},
            {'code': 'PROMO10', 'quantity': 1, 'price': 100}
        ]
        apply_promo_discount(items)
        self.assertEqual(items[0]['total'], 100)
        self.assertEqual(items[1]['total'], 90)

if __name__ == "__main__":
    unittest.main()