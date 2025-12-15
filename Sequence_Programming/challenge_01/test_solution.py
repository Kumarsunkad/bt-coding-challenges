# test_solution.py
from solution import sum_and_average

def run_tests():
    test_cases = [
        (10, 20, (30, 15.0)),       # positive numbers
        (-5, 15, (10, 5.0)),        # mix negative & positive
        (0, 0, (0, 0.0)),           # zeros
        (3.5, 2.5, (6.0, 3.0)),     # floats
        (-10, -20, (-30, -15.0))    # negative numbers
    ]

    for i, (a, b, expected) in enumerate(test_cases, 1):
        result = sum_and_average(a, b)
        assert result == expected, f"Test {i} Failed: got {result}, expected {expected}"
        print(f"Test {i} Passed ✅")

if __name__ == "__main__":
    run_tests()
