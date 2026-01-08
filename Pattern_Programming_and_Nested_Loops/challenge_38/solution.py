# solution.py

def generate_pattern(N):
    """
    Generates Fibonacci pattern: 1\n1 2\n3 5 8\n... for N rows
    """
    fib = []
    a, b = 1, 1
    count = sum(range(1, N+1))
    for _ in range(count):
        fib.append(a)
        a, b = b, a + b
    pattern = []
    idx = 0
    for row in range(1, N+1):
        row_nums = fib[idx:idx+row]
        pattern.append(' '.join(map(str, row_nums)))
        idx += row
    return '\n'.join(pattern)

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_pattern(N))