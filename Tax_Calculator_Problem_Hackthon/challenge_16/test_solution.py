# test_solution.py
import unittest
from solution import validate_name, validate_empid, validate_basic_salary, validate_allowances, validate_bonus_percentage, validate_gross_monthly, validate_annual_gross

class TestValidations(unittest.TestCase):
    def test_valid_name(self):
        self.assertTrue(validate_name("John Doe"))
        self.assertFalse(validate_name(""))
        self.assertFalse(validate_name("John123"))
        self.assertFalse(validate_name("A" * 51))

    def test_valid_empid(self):
        self.assertTrue(validate_empid("E12345"))
        self.assertFalse(validate_empid("E12"))
        self.assertFalse(validate_empid("E1234567890A"))

    def test_valid_basic_salary(self):
        self.assertTrue(validate_basic_salary(50000))
        self.assertFalse(validate_basic_salary(0))
        self.assertFalse(validate_basic_salary(10000001))

    def test_valid_allowances(self):
        self.assertTrue(validate_allowances(10000))
        self.assertTrue(validate_allowances(0))
        self.assertFalse(validate_allowances(-1))

    def test_valid_bonus_pct(self):
        self.assertTrue(validate_bonus_percentage(10))
        self.assertFalse(validate_bonus_percentage(101))

    def test_valid_gross_monthly(self):
        self.assertTrue(validate_gross_monthly(85000))
        self.assertFalse(validate_gross_monthly(0))

    def test_valid_annual_gross(self):
        self.assertTrue(validate_annual_gross(1000000))
        self.assertFalse(validate_annual_gross(10000001))

if __name__ == "__main__":
    unittest.main()