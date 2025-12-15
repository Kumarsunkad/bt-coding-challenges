# solution.py

def sum_and_average(a, b):
    """
    Function to calculate sum and average of two numbers.
    
    Args:
    a (int/float): First number
    b (int/float): Second number
    
    Returns:
    tuple: (sum, average)
    """
    total = a + b
    avg = total / 2
    return total, avg


# Test the function
if __name__ == "__main__":
    # Example inputs
    num1 = 10
    num2 = 20

    total, avg = sum_and_average(num1, num2)
    print("Sum:", total)
    print("Average:", avg)
