# test_solution.py
import unittest
from solution import transpose

class TestTranspose(unittest.TestCase):
    def test_transpose(self):
        matrix = [[1, 2], [3, 4]]
        result = transpose(matrix)
        self.assertEqual(result, [[1, 3], [2, 4]])

if __name__ == "__main__":
    unittest.main()