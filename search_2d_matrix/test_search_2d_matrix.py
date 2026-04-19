import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from search2DMatrix import search_2d


def run_tests() -> None:
    matrix = [
        [2, 7, 13, 11],
        [4, 0, 15, 1],
        [3, 14, 6, 5],
    ]

    test_cases = [
        {
            "description": "target not present in matrix",
            "matrix": matrix,
            "target": 8,
            "expected": False,
        },
        {
            "description": "target in the last row",
            "matrix": matrix,
            "target": 5,
            "expected": True,
        },
        {
            "description": "target in the first row",
            "matrix": matrix,
            "target": 7,
            "expected": True,
        },
        {
            "description": "target in the middle row",
            "matrix": matrix,
            "target": 15,
            "expected": True,
        },
        {
            "description": "empty matrix -- always False",
            "matrix": [],
            "target": 1,
            "expected": False,
        },
        {
            "description": "single element matrix -- target found",
            "matrix": [[42]],
            "target": 42,
            "expected": True,
        },
        {
            "description": "single element matrix -- target not found",
            "matrix": [[42]],
            "target": 1,
            "expected": False,
        },
        {
            "description": "target is zero",
            "matrix": matrix,
            "target": 0,
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = search_2d(test["matrix"], test["target"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  target:   " + str(test["target"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
