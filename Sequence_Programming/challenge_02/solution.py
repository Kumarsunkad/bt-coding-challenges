# solution.py

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    SI = (P * R * T) / 100
    """
    si = (principal * rate * time) / 100
    return si

# Example usage (can remove if only for testing)
if __name__ == "__main__":
    P = float(input("Enter principal amount: "))
    R = float(input("Enter rate of interest: "))
    T = float(input("Enter time in years: "))
    print("Simple Interest:", calculate_simple_interest(P, R, T))
