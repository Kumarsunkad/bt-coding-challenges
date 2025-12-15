# solution.py

def check_even_odd(number):
    """
    Returns 'Even' if number is divisible by 2, else 'Odd'
    """
    return "Even" if number % 2 == 0 else "Odd"

# Example usage (optional)
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = check_even_odd(num)
    print(result)
