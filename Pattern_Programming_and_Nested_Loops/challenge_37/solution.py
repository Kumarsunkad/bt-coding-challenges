# solution.py

def generate_pattern(N):
    """
    Generates number pattern: 1\n12\n123\n... for N rows
    """
    pattern = []
    for i in range(1, N+1):
        row = ''.join(str(j) for j in range(1, i+1))
        pattern.append(row)
    return '\n'.join(pattern)

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_pattern(N))