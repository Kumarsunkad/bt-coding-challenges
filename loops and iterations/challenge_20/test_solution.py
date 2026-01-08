# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_10(self):
        self.assertEqual(generate_series(10), [1,2,4,7])

    def test_series_22(self):
        self.assertEqual(generate_series(22), [1,2,4,7,11,16,22])

if __name__ == "__main__":
    unittest.main()