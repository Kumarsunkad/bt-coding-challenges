# test_solution.py
import unittest
from solution import calculate_gross_salaries

class TestGrossSalaries(unittest.TestCase):
    def test_basic_calculation(self):
        result = calculate_gross_salaries("John Doe", "E12345", 80000, 5000, 10)
        self.assertEqual(result['name'], "John Doe")
        self.assertEqual(result['empid'], "E12345")
        self.assertEqual(result['gross_monthly'], 85000)
        self.assertEqual(result['annual_gross'], 85000 * 12 + 85000 * 12 * 0.1)

    def test_no_bonus(self):
        result = calculate_gross_salaries("Jane", "E67890", 70000, 3000, 0)
        self.assertEqual(result['gross_monthly'], 73000)
        self.assertEqual(result['annual_gross'], 73000 * 12)

if __name__ == "__main__":
    unittest.main()