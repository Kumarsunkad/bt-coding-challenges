# test_solution.py
import unittest
from solution import reverse_number

class TestReverse(unittest.TestCase):
    def test_123(self):
        self.assertEqual(reverse_number(123), 321)

    def test_100(self):
        self.assertEqual(reverse_number(100), 1)

if __name__ == "__main__":
    unittest.main()