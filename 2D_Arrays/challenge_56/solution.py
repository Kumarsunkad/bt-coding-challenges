# solution.py

def sum_2d(matrix):
    """
    Computes the sum of all elements in a 2D array.
    """
    return sum(sum(row) for row in matrix)

# Example usage (optional)
if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    total = sum_2d(matrix)
    print("Sum:", total)