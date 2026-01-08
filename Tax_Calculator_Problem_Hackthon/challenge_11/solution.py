# solution.py

def calculate_gross_salaries(name, empid, basic_salary, special_allowances, bonus_percentage):
    """
    Calculates gross monthly and annual salaries based on inputs.
    Returns a dictionary with employee details and calculations.
    """
    gross_monthly = basic_salary + special_allowances
    annual_gross = (gross_monthly * 12) + (gross_monthly * 12 * bonus_percentage / 100)
    return {
        'name': name,
        'empid': empid,
        'gross_monthly': gross_monthly,
        'annual_gross': annual_gross
    }

# Example usage (optional)
if __name__ == "__main__":
    name = input("Enter name: ")
    empid = input("Enter EmpID: ")
    basic = float(input("Enter Basic Monthly Salary: "))
    allowances = float(input("Enter Special Allowances (Monthly): "))
    bonus_pct = float(input("Enter Bonus Percentage: "))
    result = calculate_gross_salaries(name, empid, basic, allowances, bonus_pct)
    print(f"Name: {result['name']}")
    print(f"EmpID: {result['empid']}")
    print(f"Gross Monthly Salary: ₹{result['gross_monthly']:.2f}")
    print(f"Annual Gross Salary: ₹{result['annual_gross']:.2f}")