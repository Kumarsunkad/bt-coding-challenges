# test_solution.py
import unittest
from unittest import mock
from solution import select_services

class TestSelectServices(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['1,4'])
    def test_select(self):
        services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
        result = select_services(services)
        expected = ["General Consultation", "X-Ray"]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()