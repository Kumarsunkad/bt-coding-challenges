# solution.py

def apply_gst(total_cost):
    """
    Applies 18% GST to the total cost.
    Returns gst_amount, grand_total.
    """
    gst_rate = 0.18
    gst = total_cost * gst_rate
    grand_total = total_cost + gst
    return gst, grand_total

# Example usage (optional)
if __name__ == "__main__":
    total_cost = 2000
    gst, grand_total = apply_gst(total_cost)
    print(f"GST (18%): ₹{gst:.2f}")
    print(f"Grand Total: ₹{grand_total:.2f}")