# solution.py

def get_student_grade(name, marks):
    """
    Calculates the average grade for a student based on their marks.
    Returns a string with name, average, and letter grade.
    Grades: A (>=90), B (>=80), C (>=70), D (>=60), F (<60)
    """
    if not marks:
        return f"{name}: No marks available"
    average = sum(marks) / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return f"{name}: Average {average:.2f}, Grade {grade}"

# Example usage (optional)
if __name__ == "__main__":
    name = input("Enter student name: ")
    marks_input = input("Enter marks separated by spaces: ")
    marks = list(map(float, marks_input.split()))
    result = get_student_grade(name, marks)
    print(result)