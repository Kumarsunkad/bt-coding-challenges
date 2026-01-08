# solution.py

def calculate_net_salary(annual_gross, total_tax):
    """
    Calculates net salary after tax deductions.
    Returns net salary.
    """
    net = annual_gross - total_tax
    return net

# Example usage (optional)
if __name__ == "__main__":
    annual_gross = float(input("Enter Annual Gross Salary: "))
    total_tax = float(input("Enter Total Tax Payable: "))
    net = calculate_net_salary(annual_gross, total_tax)
    print(f"Annual Gross Salary: ₹{annual_gross:.2f}")
    print(f"Total Tax Payable: ₹{total_tax:.2f}")
    print(f"Annual Net Salary: ₹{net:.2f}")