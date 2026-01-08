# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_5(self):
        self.assertEqual(generate_series(5), [1,3,5])

    def test_series_10(self):
        self.assertEqual(generate_series(10), [1,3,5,7,9])

if __name__ == "__main__":
    unittest.main()