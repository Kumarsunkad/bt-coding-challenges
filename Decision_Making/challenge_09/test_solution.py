# test_solution.py
import unittest
from solution import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_leap_years(self):
        self.assertEqual(is_leap_year(2000), "Leap Year")
        self.assertEqual(is_leap_year(2020), "Leap Year")
        self.assertEqual(is_leap_year(2024), "Leap Year")

    def test_non_leap_years(self):
        self.assertEqual(is_leap_year(1900), "Not a Leap Year")
        self.assertEqual(is_leap_year(2021), "Not a Leap Year")
        self.assertEqual(is_leap_year(2100), "Not a Leap Year")

if __name__ == "__main__":
    unittest.main()