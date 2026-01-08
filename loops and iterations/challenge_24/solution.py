# solution.py

def generate_series(N):
    """
    Generates the Fibonacci series 1,1,2,3,5,8,13,21,... up to N
    """
    series = []
    a, b = 1, 1
    while a <= N:
        series.append(a)
        a, b = b, a + b
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))