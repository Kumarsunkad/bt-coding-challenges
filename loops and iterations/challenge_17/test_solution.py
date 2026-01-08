# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_5(self):
        self.assertEqual(generate_series(5), [1,2,3,4,5])

    def test_series_1(self):
        self.assertEqual(generate_series(1), [1])

if __name__ == "__main__":
    unittest.main()