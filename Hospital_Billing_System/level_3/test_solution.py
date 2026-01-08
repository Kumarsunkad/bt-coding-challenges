# test_solution.py
import unittest
from solution import fetch_costs

class TestFetchCosts(unittest.TestCase):
    def test_fetch(self):
        services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
        costs = [500, 300, 800, 1500, 4000, 7000]
        selected = ["General Consultation", "X-Ray"]
        result = fetch_costs(selected, services, costs)
        expected = [500, 1500]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()