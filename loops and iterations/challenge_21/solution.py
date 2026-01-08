# solution.py

def generate_series(N):
    """
    Generates the series 1,4,9,25,36,49,81,... (squares of numbers not divisible by 4) up to N
    """
    series = []
    i = 1
    while i ** 2 <= N:
        if i % 4 != 0:
            series.append(i ** 2)
        i += 1
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))