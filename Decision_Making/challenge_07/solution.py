# solution.py

def check_tax(name, salary):
    """
    Checks if salary > 3,00,000
    Returns appropriate message
    """
    if salary > 300000:
        return f"{name} must pay tax."
    else:
        return f"{name} does not need to pay tax."

# Example usage (optional)
if __name__ == "__main__":
    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    result = check_tax(name, salary)
    print(result)
