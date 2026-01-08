# test_solution.py
import unittest
from unittest import mock
from solution import create_array

class TestCreateArray(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['1', '2', '3'])
    def test_create_array_3(self):
        result = create_array(3)
        self.assertEqual(result, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()