# solution.py

import re

def validate_name(name):
    """Name: Non-empty, alphabets only, max 50 characters."""
    if not name or len(name) > 50 or not name.replace(' ', '').isalpha():
        return False
    return True

def validate_empid(empid):
    """EmpID: Alphanumeric, 5–10 characters."""
    if not re.match(r'^[a-zA-Z0-9]{5,10}$', empid):
        return False
    return True

def validate_basic_salary(salary):
    """Basic Salary: Positive number, max ₹1,00,00,000."""
    if not isinstance(salary, (int, float)) or salary <= 0 or salary > 10000000:
        return False
    return True

def validate_allowances(allowances):
    """Special Allowances: Non-negative, max ₹1,00,00,000."""
    if not isinstance(allowances, (int, float)) or allowances < 0 or allowances > 10000000:
        return False
    return True

def validate_bonus_percentage(pct):
    """Bonus Percentage: Numeric value, 0–100."""
    if not isinstance(pct, (int, float)) or pct < 0 or pct > 100:
        return False
    return True

def validate_gross_monthly(gross):
    """Gross Monthly Salary must be greater than zero."""
    return gross > 0

def validate_annual_gross(annual):
    """Annual Gross Salary should not exceed realistic values (e.g., 1 crore)."""
    return annual <= 10000000  # Assuming reasonable limit

# Example usage (optional)
if __name__ == "__main__":
    name = input("Enter name: ")
    if not validate_name(name):
        print("Invalid name")
    else:
        print("Valid name")
    # Similarly for others