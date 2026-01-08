# test_solution.py
import unittest
from solution import calculate_loyalty_points

class TestLoyaltyPoints(unittest.TestCase):
    def test_1000_spent(self):
        self.assertEqual(calculate_loyalty_points(1000), 10)

    def test_150_spent(self):
        self.assertEqual(calculate_loyalty_points(150), 1)

    def test_99_spent(self):
        self.assertEqual(calculate_loyalty_points(99), 0)

if __name__ == "__main__":
    unittest.main()