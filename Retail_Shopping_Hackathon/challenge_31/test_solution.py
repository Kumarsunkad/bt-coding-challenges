# test_solution.py
import unittest
from solution import apply_payment_surcharge

class TestPaymentSurcharge(unittest.TestCase):
    def test_cash(self):
        payable, surcharge = apply_payment_surcharge(10000, 'Cash')
        self.assertEqual(payable, 10000)
        self.assertEqual(surcharge, 0)

    def test_credit_card(self):
        payable, surcharge = apply_payment_surcharge(10000, 'Credit Card')
        self.assertEqual(payable, 10200)
        self.assertEqual(surcharge, 200)

if __name__ == "__main__":
    unittest.main()