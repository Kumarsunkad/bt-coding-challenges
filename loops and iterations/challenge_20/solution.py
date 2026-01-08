# solution.py

def generate_series(N):
    """
    Generates the series 1,2,4,7,11,16,22,... up to N
    """
    series = []
    current = 1
    increment = 1
    while current <= N:
        series.append(current)
        current += increment
        increment += 1
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))