# test_solution.py
import unittest
from solution import separate_double

class TestSeparate(unittest.TestCase):
    def test_3_14(self):
        whole, frac = separate_double(3.14)
        self.assertEqual(whole, 3)
        self.assertAlmostEqual(frac, 0.14)

    def test_10_0(self):
        whole, frac = separate_double(10.0)
        self.assertEqual(whole, 10)
        self.assertEqual(frac, 0.0)

if __name__ == "__main__":
    unittest.main()