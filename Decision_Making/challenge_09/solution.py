# solution.py

def is_leap_year(year):
    """
    Checks if the given year is a leap year.
    A year is a leap year if it is divisible by 4, but not by 100 unless also by 400.
    Returns 'Leap Year' or 'Not a Leap Year'.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example usage (optional)
if __name__ == "__main__":
    year = int(input("Enter a year: "))
    result = is_leap_year(year)
    print(result)