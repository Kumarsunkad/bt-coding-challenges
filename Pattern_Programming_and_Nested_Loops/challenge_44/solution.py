# solution.py

def reverse_number(num):
    """
    Reverses the digits of a number.
    """
    return int(str(num)[::-1])

# Example usage (optional)
if __name__ == "__main__":
    num = int(input("Enter number: "))
    rev = reverse_number(num)
    print(f"Reverse: {rev}")