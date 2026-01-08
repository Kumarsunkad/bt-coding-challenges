# test_solution.py
import unittest
from solution import matrix_multiply

class TestMatrixMultiply(unittest.TestCase):
    def test_multiply(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = matrix_multiply(A, B)
        expected = [[19, 22], [43, 50]]
        self.assertEqual(result, expected)

    def test_invalid(self):
        A = [[1, 2]]
        B = [[1], [2], [3]]
        self.assertIsNone(matrix_multiply(A, B))

if __name__ == "__main__":
    unittest.main()