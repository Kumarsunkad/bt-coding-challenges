# solution.py

def calculate_total_cost(selected_costs):
    """
    Calculates the total cost from selected costs.
    """
    return sum(selected_costs)

# Example usage (optional)
if __name__ == "__main__":
    selected_costs = [500, 1500]
    total = calculate_total_cost(selected_costs)
    print("Total Cost (Before Tax): ₹", total)