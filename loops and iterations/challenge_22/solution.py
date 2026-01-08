# solution.py

def generate_series(N):
    """
    Generates the series 1,4,7,12,23,... up to N
    """
    series = [1]
    current = 1
    # Increments: 3,3,5,11,13,17,19,23,...
    increments = [3,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for inc in increments:
        current += inc
        if current > N:
            break
        series.append(current)
    return series

# Example usage (optional)
if __name__ == "__main__":
    N = int(input("Enter N: "))
    print(generate_series(N))