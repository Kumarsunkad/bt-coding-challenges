# solution.py

def apply_discounts(subtotal, age):
    """
    Applies senior citizen (10% if age >=60) and high-bill (5% if subtotal >5000) discounts.
    Returns discounted_subtotal, total_discount.
    """
    discount = 0
    if age >= 60:
        discount += subtotal * 0.10
    if subtotal > 5000:
        discount += subtotal * 0.05
    discounted_subtotal = subtotal - discount
    return discounted_subtotal, discount

# Example usage (optional)
if __name__ == "__main__":
    subtotal = 6000
    age = 65
    discounted, disc = apply_discounts(subtotal, age)
    print(f"Discounted Subtotal: ₹{discounted:.2f}, Discount: ₹{disc:.2f}")