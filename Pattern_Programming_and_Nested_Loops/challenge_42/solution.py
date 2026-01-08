# solution.py

def generate_series(N):
    """
    Generates series 1, -5, 9, -13, 17, -21, ... up to N terms
    """
    series = []
    for n in range(1, N+1):
        term = ((-1)**(n+1)) * (4*n - 3)
        series.append(term)
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))