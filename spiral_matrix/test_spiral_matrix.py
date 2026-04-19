import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from spiral_matrix import spiral_order


def run_tests() -> None:
    test_cases = [
        {
            "description": "3x3 matrix -- spiral inward",
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
        },
        {
            "description": "3x4 matrix -- non-square",
            "input": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        },
        {
            "description": "1x1 matrix -- single element",
            "input": [[1]],
            "expected": [1],
        },
        {
            "description": "2x2 matrix",
            "input": [[1, 2], [3, 4]],
            "expected": [1, 2, 4, 3],
        },
        {
            "description": "1x4 row matrix -- just the top row",
            "input": [[1, 2, 3, 4]],
            "expected": [1, 2, 3, 4],
        },
        {
            "description": "4x1 column matrix -- top to bottom",
            "input": [[1], [2], [3], [4]],
            "expected": [1, 2, 3, 4],
        },
        {
            "description": "4x4 matrix",
            "input": [
                [1,  2,  3,  4],
                [5,  6,  7,  8],
                [9,  10, 11, 12],
                [13, 14, 15, 16],
            ],
            "expected": [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = spiral_order(test["input"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
