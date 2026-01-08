# solution.py

def generate_pattern(N):
    """
    Generates number pattern: 1\n22\n333\n... for N rows
    """
    pattern = []
    for i in range(1, N+1):
        pattern.append(str(i) * i)
    return '\n'.join(pattern)

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_pattern(N))