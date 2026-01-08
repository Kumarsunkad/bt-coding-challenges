# solution.py

def generate_report(name, empid, gross_monthly, annual_gross, taxable_income, total_tax, net_salary):
    """
    Generates a formatted report string.
    """
    report = f"""
Employee Tax Report
Name: {name}
EmpID: {empid}
Gross Monthly Salary: ₹{gross_monthly:.2f}
Annual Gross Salary: ₹{annual_gross:.2f}
Taxable Income: ₹{taxable_income:.2f}
Tax Payable: ₹{total_tax:.2f}
Annual Net Salary: ₹{net_salary:.2f}
"""
    return report.strip()

# Example usage (optional)
if __name__ == "__main__":
    # Assuming inputs or from previous calculations
    name = "John Doe"
    empid = "E12345"
    gross_monthly = 85000
    annual_gross = 1020000
    taxable_income = 970000
    total_tax = 76800
    net_salary = 943200
    report = generate_report(name, empid, gross_monthly, annual_gross, taxable_income, total_tax, net_salary)
    print(report)