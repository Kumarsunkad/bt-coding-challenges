# solution.py

def search_2d(matrix, element):
    """
    Checks if a given element exists in the 2D array.
    """
    for row in matrix:
        if element in row:
            return True
    return False

# Example usage (optional)
if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    elem = int(input("Enter element to search: "))
    found = search_2d(matrix, elem)
    print("Found:", found)