# solution.py

def display_services(services):
    """
    Displays the list of services.
    """
    for i, service in enumerate(services, 1):
        print(f"{i}. {service}")

def select_services(services):
    """
    Allows patient to select services by numbers.
    Returns list of selected service names.
    """
    selections = input("Enter selected service numbers (comma-separated): ")
    indices = [int(x.strip()) - 1 for x in selections.split(',')]
    selected = [services[i] for i in indices]
    return selected

# Example usage (optional)
if __name__ == "__main__":
    services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
    display_services(services)
    selected = select_services(services)
    print("Selected Services:", selected)