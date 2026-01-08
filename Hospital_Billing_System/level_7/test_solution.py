# test_solution.py
import unittest
from solution import setup_services

class TestSetupServices(unittest.TestCase):
    def test_setup(self):
        services, costs = setup_services()
        expected_services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
        expected_costs = [500, 300, 800, 1500, 4000, 7000]
        self.assertEqual(services, expected_services)
        self.assertEqual(costs, expected_costs)

if __name__ == "__main__":
    unittest.main()