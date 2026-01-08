# test_solution.py
import unittest
from solution import generate_invoice

class TestGenerateInvoice(unittest.TestCase):
    def test_invoice(self):
        patient = {'name': 'Arjun Kumar', 'age': 35, 'gender': 'Male', 'contact': '9876543210'}
        selected_services = ["General Consultation", "X-Ray"]
        selected_costs = [500, 1500]
        subtotal = 2000
        gst = 360
        grand_total = 2360
        invoice = generate_invoice(patient, selected_services, selected_costs, subtotal, gst, grand_total)
        self.assertIn("Arjun Kumar", invoice)
        self.assertIn("General Consultation: ₹500", invoice)
        self.assertIn("Grand Total: ₹2360.00", invoice)

if __name__ == "__main__":
    unittest.main()