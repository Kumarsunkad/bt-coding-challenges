# test_solution.py
import unittest
from solution import generate_pattern

class TestPattern(unittest.TestCase):
    def test_n_3(self):
        expected = "11111\n22222\n33333"
        self.assertEqual(generate_pattern(3), expected)

if __name__ == "__main__":
    unittest.main()