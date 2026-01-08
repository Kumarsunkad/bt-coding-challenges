# solution.py

def calculate_tax(grand_total):
    """
    Calculates tax based on grand total:
    <5000: 5%, 5000-20000: 10%, >20000: 15%
    Returns total_with_tax, tax_amount.
    """
    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    tax = grand_total * tax_rate
    total_with_tax = grand_total + tax
    return total_with_tax, tax

# Example usage (optional)
if __name__ == "__main__":
    grand_total = float(input("Enter grand total after discounts: "))
    total_with_tax, tax = calculate_tax(grand_total)
    print(f"Total with Tax: ₹{total_with_tax:.2f}, Tax: ₹{tax:.2f}")