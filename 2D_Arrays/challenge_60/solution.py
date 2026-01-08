# solution.py

def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B.
    Returns the result matrix or None if invalid dimensions.
    """
    if not A or not B or len(A[0]) != len(B):
        return None
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example usage (optional)
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = matrix_multiply(A, B)
    if result:
        for row in result:
            print(row)
    else:
        print("Invalid dimensions")