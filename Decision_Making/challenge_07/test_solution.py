# test_solution.py
import unittest
from solution import check_tax

class TestTaxEligibility(unittest.TestCase):
    def test_below_threshold(self):
        self.assertEqual(check_tax("Ramesh", 250000), "Ramesh does not need to pay tax.")
        self.assertEqual(check_tax("Anita", 300000), "Anita does not need to pay tax.")

    def test_above_threshold(self):
        self.assertEqual(check_tax("Sita", 450000), "Sita must pay tax.")
        self.assertEqual(check_tax("Rahul", 500000), "Rahul must pay tax.")

if __name__ == "__main__":
    unittest.main()
