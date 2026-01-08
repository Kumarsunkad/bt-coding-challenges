# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_50(self):
        self.assertEqual(generate_series(50), [1,4,9,25,36,49])

    def test_series_100(self):
        self.assertEqual(generate_series(100), [1,4,9,25,36,49,81,100])

if __name__ == "__main__":
    unittest.main()