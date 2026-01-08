# test_solution.py
import unittest
from solution import get_student_grade

class TestStudentGrade(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(get_student_grade("Alice", [95, 92, 98]), "Alice: Average 95.00, Grade A")

    def test_grade_b(self):
        self.assertEqual(get_student_grade("Bob", [85, 82, 88]), "Bob: Average 85.00, Grade B")

    def test_grade_c(self):
        self.assertEqual(get_student_grade("Charlie", [75, 72, 78]), "Charlie: Average 75.00, Grade C")

    def test_grade_d(self):
        self.assertEqual(get_student_grade("David", [65, 62, 68]), "David: Average 65.00, Grade D")

    def test_grade_f(self):
        self.assertEqual(get_student_grade("Eve", [55, 52, 58]), "Eve: Average 55.00, Grade F")

    def test_no_marks(self):
        self.assertEqual(get_student_grade("Frank", []), "Frank: No marks available")

if __name__ == "__main__":
    unittest.main()