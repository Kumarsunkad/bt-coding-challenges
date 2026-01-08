# test_solution.py
import unittest
from solution import generate_series

class TestSeries(unittest.TestCase):
    def test_series_13(self):
        self.assertEqual(generate_series(13), [1,1,2,3,5,8,13])

    def test_series_20(self):
        self.assertEqual(generate_series(20), [1,1,2,3,5,8,13])

if __name__ == "__main__":
    unittest.main()