# solution.py

def calculate_discount(total_amount, discount_percent):
    """
    Calculate the final amount after applying discount.

    final_amount = total_amount - (total_amount * discount_percent / 100)
    """
    discount_amount = total_amount * discount_percent / 100
    final_amount = total_amount - discount_amount
    return final_amount

# Example usage (optional, can remove if only for testing)
if __name__ == "__main__":
    total = float(input("Enter total amount: "))
    discount = float(input("Enter discount percentage: "))
    print("Final Amount after discount:", calculate_discount(total, discount))
