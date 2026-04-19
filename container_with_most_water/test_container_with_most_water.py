import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from container_with_most_water import max_area


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- walls at index 1 and 8 give area 49",
            "input": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49,
        },
        {
            "description": "two walls -- only one container possible",
            "input": [1, 1],
            "expected": 1,
        },
        {
            "description": "symmetric heights -- outer walls are best",
            "input": [4, 3, 2, 1, 4],
            "expected": 16,
        },
        {
            "description": "two equal tall walls with short walls between",
            "input": [1, 2, 1],
            "expected": 2,
        },
        {
            "description": "increasing heights -- best is outermost pair",
            "input": [1, 2, 3, 4, 5],
            "expected": 6,
        },
        {
            "description": "decreasing heights",
            "input": [5, 4, 3, 2, 1],
            "expected": 6,
        },
        {
            "description": "tall walls near the center -- width matters",
            "input": [2, 3, 4, 5, 18, 17, 6],
            "expected": 17,
        },
        {
            "description": "all same height -- widest span wins",
            "input": [5, 5, 5, 5, 5],
            "expected": 20,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = max_area(test["input"])
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
