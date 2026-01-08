# solution.py

def collect_patient_details():
    """
    Collects patient details: name, age, gender, contact.
    Returns a dict.
    """
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    contact = input("Contact: ")
    return {'name': name, 'age': age, 'gender': gender, 'contact': contact}

# Example usage (optional)
if __name__ == "__main__":
    patient = collect_patient_details()
    print(patient)