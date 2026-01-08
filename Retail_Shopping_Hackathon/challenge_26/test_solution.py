# test_solution.py
import unittest
from solution import calculate_grand_total

class TestGrandTotal(unittest.TestCase):
    def test_multiple_items(self):
        items = [{'quantity': 2, 'price': 50}, {'quantity': 3, 'price': 30}]
        self.assertEqual(calculate_grand_total(items), 190)

    def test_empty_list(self):
        self.assertEqual(calculate_grand_total([]), 0)

if __name__ == "__main__":
    unittest.main()