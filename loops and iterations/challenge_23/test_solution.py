# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_41(self):
        self.assertEqual(generate_series(41), [1,5,9,13,17,21,25,29,33,37,41])

    def test_series_10(self):
        self.assertEqual(generate_series(10), [1,5,9])

if __name__ == "__main__":
    unittest.main()