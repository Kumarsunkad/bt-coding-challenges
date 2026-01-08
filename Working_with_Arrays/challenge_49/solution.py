# solution.py

def search_element(arr, element):
    """
    Searches for the given element in the array.
    Returns True if found, False otherwise.
    """
    return element in arr

# Example usage (optional)
if __name__ == "__main__":
    arr = [5, 2, 8, 1]
    elem = int(input("Enter element to search: "))
    found = search_element(arr, elem)
    print("Found:", found)