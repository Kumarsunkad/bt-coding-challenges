# solution.py

def calculate_loyalty_points(final_total):
    """
    Calculates loyalty points: 1 point per ₹100 spent.
    Returns the points.
    """
    return int(final_total // 100)

# Example usage (optional)
if __name__ == "__main__":
    final_total = float(input("Enter final total: "))
    points = calculate_loyalty_points(final_total)
    print(f"Loyalty Points Earned: {points}")