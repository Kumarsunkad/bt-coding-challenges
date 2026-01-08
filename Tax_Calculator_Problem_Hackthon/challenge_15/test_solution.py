# test_solution.py
import unittest
from solution import generate_report

class TestReportGeneration(unittest.TestCase):
    def test_report_format(self):
        report = generate_report("John Doe", "E12345", 85000, 1020000, 970000, 76800, 943200)
        self.assertIn("Name: John Doe", report)
        self.assertIn("EmpID: E12345", report)
        self.assertIn("Gross Monthly Salary: ₹85000.00", report)
        self.assertIn("Annual Gross Salary: ₹1020000.00", report)
        self.assertIn("Taxable Income: ₹970000.00", report)
        self.assertIn("Tax Payable: ₹76800.00", report)
        self.assertIn("Annual Net Salary: ₹943200.00", report)

if __name__ == "__main__":
    unittest.main()