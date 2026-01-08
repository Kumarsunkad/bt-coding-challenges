# solution.py

def setup_services():
    """
    Sets up the services and costs arrays.
    Returns services, costs.
    """
    services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
    costs = [500, 300, 800, 1500, 4000, 7000]
    return services, costs

# Example usage (optional)
if __name__ == "__main__":
    services, costs = setup_services()
    print("Services:", services)
    print("Costs:", costs)