# solution.py

def check_minimum_purchase(final_total):
    """
    Checks if final_total >= 500.
    Returns True if met, False otherwise.
    """
    return final_total >= 500

# Example usage (optional)
if __name__ == "__main__":
    final_total = float(input("Enter final total: "))
    if check_minimum_purchase(final_total):
        print("Minimum purchase met.")
    else:
        print("Minimum purchase not met. Invoice cannot be generated.")