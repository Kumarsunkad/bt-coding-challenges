# solution.py

def swap_numbers(a, b):
    """
    Swap two numbers and return them.
    Can be done using tuple unpacking.
    """
    return b, a

# Example usage (optional for testing)
if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    a, b = swap_numbers(a, b)
    print("After swapping:")
    print("a =", a)
    print("b =", b)
