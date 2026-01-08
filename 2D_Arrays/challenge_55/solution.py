# solution.py

def create_2d_array(rows, cols):
    """
    Creates a 2D array of size rows x cols.
    """
    matrix = []
    for i in range(rows):
        row = [int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)]
        matrix.append(row)
    return matrix

def display_row_wise(matrix):
    """
    Displays the 2D array row-wise.
    """
    for row in matrix:
        print(' '.join(map(str, row)))

# Example usage (optional)
if __name__ == "__main__":
    rows = int(input("Enter rows: "))
    cols = int(input("Enter cols: "))
    matrix = create_2d_array(rows, cols)
    display_row_wise(matrix)