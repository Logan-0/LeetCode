import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from missing_number import missing_number


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- 2 is missing from [0,1,2,3]",
            "input": [3, 0, 1],
            "expected": 2,
        },
        {
            "description": "missing the last number in range",
            "input": [0, 1],
            "expected": 2,
        },
        {
            "description": "larger array -- 8 is missing",
            "input": [9, 6, 4, 2, 3, 5, 7, 0, 1],
            "expected": 8,
        },
        {
            "description": "single element -- 0 is present, 1 is missing",
            "input": [0],
            "expected": 1,
        },
        {
            "description": "single element -- 1 is present, 0 is missing",
            "input": [1],
            "expected": 0,
        },
        {
            "description": "missing the first number (zero)",
            "input": [1, 2, 3],
            "expected": 0,
        },
        {
            "description": "sorted array, middle element missing",
            "input": [0, 1, 2, 3, 5],
            "expected": 4,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = missing_number(list(test["input"]))
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  input:    " + str(test["input"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
