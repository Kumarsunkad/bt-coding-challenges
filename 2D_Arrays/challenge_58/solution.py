# solution.py

def create_matrix(m, n):
    """
    Stores elements into a M x N matrix.
    """
    matrix = []
    for i in range(m):
        row = [int(input(f"Enter [{i}][{j}]: ")) for j in range(n)]
        matrix.append(row)
    return matrix

def transpose(matrix):
    """
    Returns the transpose of the matrix.
    """
    return [list(row) for row in zip(*matrix)]

def display_matrix(matrix):
    """
    Displays the matrix.
    """
    for row in matrix:
        print(' '.join(map(str, row)))

# Example usage (optional)
if __name__ == "__main__":
    m = int(input("Enter M: "))
    n = int(input("Enter N: "))
    matrix = create_matrix(m, n)
    print("Matrix:")
    display_matrix(matrix)
    trans = transpose(matrix)
    print("Transpose:")
    display_matrix(trans)