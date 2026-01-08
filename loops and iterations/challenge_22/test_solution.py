# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_23(self):
        self.assertEqual(generate_series(23), [1,4,7,12,23])

    def test_series_30(self):
        self.assertEqual(generate_series(30), [1,4,7,12,23])

if __name__ == "__main__":
    unittest.main()