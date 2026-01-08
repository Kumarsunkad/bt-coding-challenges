# test_solution.py
import unittest
from solution import apply_gst

class TestApplyGST(unittest.TestCase):
    def test_gst(self):
        gst, grand_total = apply_gst(2000)
        self.assertAlmostEqual(gst, 360)
        self.assertAlmostEqual(grand_total, 2360)

if __name__ == "__main__":
    unittest.main()