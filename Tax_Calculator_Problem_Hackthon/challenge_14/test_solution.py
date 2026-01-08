# test_solution.py
import unittest
from solution import calculate_net_salary

class TestNetSalary(unittest.TestCase):
    def test_net_calculation(self):
        self.assertEqual(calculate_net_salary(1000000, 100000), 900000)

    def test_no_tax(self):
        self.assertEqual(calculate_net_salary(500000, 0), 500000)

if __name__ == "__main__":
    unittest.main()