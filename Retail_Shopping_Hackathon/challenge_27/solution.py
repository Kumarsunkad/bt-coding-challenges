# solution.py

def apply_discounts(grand_total, total_quantity):
    """
    Applies discounts: 10% if grand_total > 10000, additional 5% if total_quantity > 20.
    Returns discounted_total, total_discount.
    """
    discount = 0
    if grand_total > 10000:
        discount += grand_total * 0.10
    if total_quantity > 20:
        discount += grand_total * 0.05  # Note: on original or after? Assuming on original as per rules
    discounted_total = grand_total - discount
    return discounted_total, discount

# Example usage (optional)
if __name__ == "__main__":
    grand_total = float(input("Enter grand total: "))
    total_quantity = int(input("Enter total quantity: "))
    discounted, disc = apply_discounts(grand_total, total_quantity)
    print(f"Discounted Total: ₹{discounted:.2f}, Discount: ₹{disc:.2f}")