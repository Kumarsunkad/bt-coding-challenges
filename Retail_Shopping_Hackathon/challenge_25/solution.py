# solution.py

def calculate_item_total(code, description, quantity, price):
    """
    Calculates the total cost for a single item.
    Returns the total.
    """
    return quantity * price

# Example usage (optional)
if __name__ == "__main__":
    code = input("Enter item code: ")
    description = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    total = calculate_item_total(code, description, quantity, price)
    print(f"Total for {description}: ₹{total:.2f}")