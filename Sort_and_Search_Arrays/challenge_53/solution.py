# solution.py

def sort_array(arr, order):
    """
    Sorts the array in ascending or descending order based on input.
    """
    if order.lower() == 'ascending':
        return sorted(arr)
    elif order.lower() == 'descending':
        return sorted(arr, reverse=True)
    else:
        return arr  # unchanged

# Example usage (optional)
if __name__ == "__main__":
    arr = [3, 1, 4, 2]
    order = input("Enter order (ascending/descending): ")
    sorted_arr = sort_array(arr, order)
    print("Sorted:", sorted_arr)