# solution.py

def fetch_costs(selected_services, services, costs):
    """
    Fetches costs for selected services.
    Returns list of costs.
    """
    selected_costs = []
    for service in selected_services:
        index = services.index(service)
        selected_costs.append(costs[index])
    return selected_costs

# Example usage (optional)
if __name__ == "__main__":
    services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
    costs = [500, 300, 800, 1500, 4000, 7000]
    selected = ["General Consultation", "X-Ray"]
    selected_costs = fetch_costs(selected, services, costs)
    print("Selected Costs:", selected_costs)