# solution.py

def create_array(n):
    """
    Accepts n and stores elements into an array of size n.
    """
    return [int(input(f"Enter element {i+1}: ")) for i in range(n)]

# Example usage (optional)
if __name__ == "__main__":
    n = int(input("Enter n: "))
    arr = create_array(n)
    print("Array:", arr)