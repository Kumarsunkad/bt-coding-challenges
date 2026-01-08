# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_36(self):
        self.assertEqual(generate_series(36), [4,16,36])

    def test_series_100(self):
        self.assertEqual(generate_series(100), [4,16,36,64,100])

if __name__ == "__main__":
    unittest.main()