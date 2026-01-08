# solution.py

def generate_series(N):
    """
    Generates the series 1,5,9,13,21,25,29,37,41,... (numbers ≡1 mod 4) up to N
    """
    series = []
    for i in range(1, N+1):
        if i % 4 == 1:
            series.append(i)
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))