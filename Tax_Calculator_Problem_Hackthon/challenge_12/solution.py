# solution.py

def calculate_taxable_income(annual_gross):
    """
    Calculates taxable income after standard deduction of ₹50,000.
    Returns taxable income.
    """
    deduction = 50000
    taxable = max(0, annual_gross - deduction)
    return taxable

# Example usage (optional)
if __name__ == "__main__":
    annual_gross = float(input("Enter Annual Gross Salary: "))
    taxable = calculate_taxable_income(annual_gross)
    print(f"Gross Salary: ₹{annual_gross:.2f}")
    print(f"Standard Deduction: ₹50,000")
    print(f"Taxable Income: ₹{taxable:.2f}")