# solution.py

def apply_membership_discount(discounted_total, is_member):
    """
    Applies 2% membership discount if is_member is True.
    Returns final_total, membership_discount.
    """
    if is_member:
        discount = discounted_total * 0.02
        final_total = discounted_total - discount
        return final_total, discount
    else:
        return discounted_total, 0

# Example usage (optional)
if __name__ == "__main__":
    discounted_total = float(input("Enter discounted total: "))
    is_member = input("Is member? (y/n): ").lower() == 'y'
    final, disc = apply_membership_discount(discounted_total, is_member)
    print(f"Final Total: ₹{final:.2f}, Membership Discount: ₹{disc:.2f}")