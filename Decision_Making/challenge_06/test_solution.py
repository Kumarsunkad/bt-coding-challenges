# test_solution.py
import unittest
from solution import check_even_odd

class TestEvenOdd(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(check_even_odd(2), "Even")
        self.assertEqual(check_even_odd(100), "Even")
        self.assertEqual(check_even_odd(0), "Even")

    def test_odd_numbers(self):
        self.assertEqual(check_even_odd(1), "Odd")
        self.assertEqual(check_even_odd(99), "Odd")
        self.assertEqual(check_even_odd(-5), "Odd")

if __name__ == "__main__":
    unittest.main()
