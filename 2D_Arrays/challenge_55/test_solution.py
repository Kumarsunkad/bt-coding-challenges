# test_solution.py
import unittest
from unittest import mock
from solution import create_2d_array

class TestCreate2DArray(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_create_2x2(self):
        result = create_2d_array(2, 2)
        self.assertEqual(result, [[1, 2], [3, 4]])

if __name__ == "__main__":
    unittest.main()