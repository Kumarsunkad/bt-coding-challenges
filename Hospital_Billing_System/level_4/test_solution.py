# test_solution.py
import unittest
from solution import calculate_total_cost

class TestCalculateTotalCost(unittest.TestCase):
    def test_total(self):
        selected_costs = [500, 1500]
        result = calculate_total_cost(selected_costs)
        self.assertEqual(result, 2000)

if __name__ == "__main__":
    unittest.main()