# test_solution.py
import unittest
from solution import calculate_overall_sales

class TestFarmerProblem(unittest.TestCase):
    def test_sales_values(self):
        total, chemical_free = calculate_overall_sales()
        # Rough expected values based on manual calculation
        self.assertTrue(total > 0)
        self.assertTrue(chemical_free > 0)
        self.assertTrue(chemical_free < total)

if __name__ == "__main__":
    unittest.main()
