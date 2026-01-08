# test_solution.py
import unittest
from solution import apply_membership_discount

class TestMembershipDiscount(unittest.TestCase):
    def test_member(self):
        total, disc = apply_membership_discount(10000, True)
        self.assertEqual(total, 9800)
        self.assertEqual(disc, 200)

    def test_non_member(self):
        total, disc = apply_membership_discount(10000, False)
        self.assertEqual(total, 10000)
        self.assertEqual(disc, 0)

if __name__ == "__main__":
    unittest.main()