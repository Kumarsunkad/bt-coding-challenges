# solution.py

def generate_invoice(patient, selected_services, selected_costs, subtotal, gst, grand_total):
    """
    Generates a detailed invoice string.
    """
    invoice = f"""
-----------------------------------------------
HealWell Care Hospital
Patient Invoice
-----------------------------------------------
Patient Information:
Name: {patient['name']}
Age: {patient['age']}
Gender: {patient['gender']}
Contact: {patient['contact']}
Services Availed:
"""
    for i, (service, cost) in enumerate(zip(selected_services, selected_costs), 1):
        invoice += f"{i}. {service}: ₹{cost}\n"
    invoice += f"""
Subtotal: ₹{subtotal}
GST (18%): ₹{gst:.2f}
Grand Total: ₹{grand_total:.2f}
Thank you for choosing HealWell Care Hospital!
-----------------------------------------------
"""
    return invoice.strip()

# Example usage (optional)
if __name__ == "__main__":
    patient = {'name': 'Arjun Kumar', 'age': 35, 'gender': 'Male', 'contact': '9876543210'}
    selected_services = ["General Consultation", "X-Ray"]
    selected_costs = [500, 1500]
    subtotal = 2000
    gst = 360
    grand_total = 2360
    invoice = generate_invoice(patient, selected_services, selected_costs, subtotal, gst, grand_total)
    print(invoice)