# solution.py

def apply_promo_discount(items):
    """
    Applies 10% discount to items with code 'PROMO10'.
    Modifies items in place, adding 'total' key.
    Returns the modified items.
    """
    for item in items:
        total = item['quantity'] * item['price']
        if item['code'] == 'PROMO10':
            total *= 0.9
        item['total'] = total
    return items

# Example usage (optional)
if __name__ == "__main__":
    items = [
        {'code': 'A1', 'quantity': 2, 'price': 50},
        {'code': 'PROMO10', 'quantity': 1, 'price': 100}
    ]
    apply_promo_discount(items)
    grand_total = sum(item['total'] for item in items)
    print(f"Grand Total after Promo: ₹{grand_total:.2f}")