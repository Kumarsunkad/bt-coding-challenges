# test_solution.py
import unittest
from solution import calculate_item_total

class TestItemTotal(unittest.TestCase):
    def test_basic_total(self):
        self.assertEqual(calculate_item_total("A1", "Apple", 2, 50), 100)

    def test_zero_quantity(self):
        self.assertEqual(calculate_item_total("B2", "Banana", 0, 30), 0)

if __name__ == "__main__":
    unittest.main()