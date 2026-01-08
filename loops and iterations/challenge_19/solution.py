# solution.py

def generate_series(N):
    """
    Generates the series 4,16,36,64,... up to N
    """
    series = []
    k = 1
    while True:
        term = (2 * k) ** 2
        if term > N:
            break
        series.append(term)
        k += 1
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))