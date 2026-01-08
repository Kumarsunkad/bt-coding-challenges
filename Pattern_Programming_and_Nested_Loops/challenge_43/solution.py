# solution.py

def separate_double(value):
    """
    Separates whole and fractional parts of a double value.
    Returns whole, fractional.
    """
    whole = int(value)
    fractional = value - whole
    return whole, fractional

# Example usage (optional)
if __name__ == "__main__":
    value = float(input("Enter double value: "))
    whole, frac = separate_double(value)
    print(f"Whole: {whole}, Fractional: {frac}")