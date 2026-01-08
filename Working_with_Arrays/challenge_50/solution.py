# solution.py

def count_odd_even(arr):
    """
    Counts the number of odd and even numbers in the array.
    Returns (odd_count, even_count)
    """
    odd = sum(1 for x in arr if x % 2 != 0)
    even = len(arr) - odd
    return odd, even

# Example usage (optional)
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    odd, even = count_odd_even(arr)
    print(f"Odd: {odd}, Even: {even}")