# solution.py

def generate_series(N):
    """
    Generates the series 1,2,3,...,N
    """
    series = []
    for i in range(1, N+1):
        series.append(i)
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))