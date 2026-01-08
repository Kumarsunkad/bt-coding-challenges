# test_solution.py
import unittest
from unittest import mock
from solution import collect_patient_details

class TestCollectPatientDetails(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['Arjun Kumar', '35', 'Male', '9876543210'])
    def test_collect(self):
        result = collect_patient_details()
        expected = {'name': 'Arjun Kumar', 'age': 35, 'gender': 'Male', 'contact': '9876543210'}
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()