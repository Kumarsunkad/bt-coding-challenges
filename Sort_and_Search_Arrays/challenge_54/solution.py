# solution.py

def binary_search(arr, target):
    """
    Implements binary search on the sorted array.
    Returns True if found, False otherwise.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Example usage (optional)
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  # assume sorted
    target = int(input("Enter target: "))
    found = binary_search(arr, target)
    print("Found:", found)