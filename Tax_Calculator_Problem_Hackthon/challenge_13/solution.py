# solution.py

def calculate_tax(taxable_income):
    """
    Calculates tax payable with New Tax Regime slabs, rebate, and cess.
    Returns total tax, base tax, cess.
    """
    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = 300000 * 0.05 + (taxable_income - 600000) * 0.10
    elif taxable_income <= 1200000:
        tax = 300000 * 0.05 + 300000 * 0.10 + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        tax = 300000 * 0.05 + 300000 * 0.10 + 300000 * 0.15 + (taxable_income - 1200000) * 0.20
    else:
        tax = 300000 * 0.05 + 300000 * 0.10 + 300000 * 0.15 + 300000 * 0.20 + (taxable_income - 1500000) * 0.30

    # Rebate if taxable <= 700000
    if taxable_income <= 700000:
        tax = 0

    cess = tax * 0.04
    total_tax = tax + cess
    return total_tax, tax, cess

# Example usage (optional)
if __name__ == "__main__":
    taxable = float(input("Enter Taxable Income: "))
    total, base, cess = calculate_tax(taxable)
    print(f"Taxable Income: ₹{taxable:.2f}")
    print(f"Base Tax: ₹{base:.2f}")
    print(f"Health and Education Cess (4%): ₹{cess:.2f}")
    print(f"Total Tax Payable: ₹{total:.2f}")