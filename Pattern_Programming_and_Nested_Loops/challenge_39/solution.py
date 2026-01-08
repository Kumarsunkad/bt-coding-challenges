# solution.py

def generate_pattern(N):
    """
    Generates perfect squares with alternating signs: 1\n-4 9\n-16 25 -36\n... for N rows
    """
    nums = []
    k = 1
    count = sum(range(1, N+1))
    for _ in range(count):
        sign = (-1)**(k+1)
        num = sign * (k ** 2)
        nums.append(num)
        k += 1
    pattern = []
    idx = 0
    for row in range(1, N+1):
        row_nums = nums[idx:idx+row]
        pattern.append(' '.join(map(str, row_nums)))
        idx += row
    return '\n'.join(pattern)

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_pattern(N))