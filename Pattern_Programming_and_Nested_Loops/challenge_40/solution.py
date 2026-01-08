# solution.py

import math

def generate_pattern(N):
    """
    Generates factorial pattern: 1\n1 2\n6 24 120\n... for N rows
    """
    pattern = []
    start = 1
    for row in range(1, N+1):
        row_nums = []
        for j in range(row):
            fact = math.factorial(start + j - 1)
            row_nums.append(fact)
        pattern.append(' '.join(map(str, row_nums)))
        start += row
    return '\n'.join(pattern)

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_pattern(N))