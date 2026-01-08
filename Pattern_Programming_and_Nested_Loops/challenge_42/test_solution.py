# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_n_6(self):
        expected = [1, -5, 9, -13, 17, -21]
        self.assertEqual(generate_series(6), expected)

if __name__ == "__main__":
    unittest.main()