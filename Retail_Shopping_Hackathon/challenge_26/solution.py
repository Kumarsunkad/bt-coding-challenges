# solution.py

def calculate_grand_total(items):
    """
    Calculates the grand total from a list of items.
    Each item is a dict with 'quantity' and 'price'.
    Returns the grand total.
    """
    total = 0
    for item in items:
        total += item['quantity'] * item['price']
    return total

# Example usage (optional)
if __name__ == "__main__":
    items = []
    while True:
        qty = int(input("Enter quantity (0 to stop): "))
        if qty == 0:
            break
        price = float(input("Enter price: "))
        items.append({'quantity': qty, 'price': price})
    grand_total = calculate_grand_total(items)
    print(f"Grand Total: ₹{grand_total:.2f}")