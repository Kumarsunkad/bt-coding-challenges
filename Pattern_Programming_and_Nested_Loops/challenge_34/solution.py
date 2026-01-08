# solution.py

def generate_pattern(N):
    """
    Generates number pattern: 12345\n12345\n... for N rows
    """
    return '\n'.join(['12345' for _ in range(N)])

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_pattern(N))