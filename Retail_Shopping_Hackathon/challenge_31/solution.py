# solution.py

def apply_payment_surcharge(final_total, payment_mode):
    """
    Applies 2% surcharge for Credit Card.
    Returns final_payable, surcharge.
    """
    if payment_mode.lower() == 'credit card':
        surcharge = final_total * 0.02
        final_payable = final_total + surcharge
        return final_payable, surcharge
    else:
        return final_total, 0

# Example usage (optional)
if __name__ == "__main__":
    final_total = float(input("Enter final total: "))
    payment_mode = input("Enter payment mode (Cash/Credit Card): ")
    payable, surcharge = apply_payment_surcharge(final_total, payment_mode)
    print(f"Final Payable: ₹{payable:.2f}, Surcharge: ₹{surcharge:.2f}")