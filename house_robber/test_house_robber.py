import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from house_robber import rob


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- rob houses 1 and 3: 1+3=4",
            "input": [1, 2, 3, 1],
            "expected": 4,
        },
        {
            "description": "rob houses 1, 3, 5: 2+9+1=12",
            "input": [2, 7, 9, 3, 1],
            "expected": 12,
        },
        {
            "description": "single house -- rob it",
            "input": [5],
            "expected": 5,
        },
        {
            "description": "two houses -- rob the larger",
            "input": [1, 2],
            "expected": 2,
        },
        {
            "description": "two houses equal value -- rob either",
            "input": [3, 3],
            "expected": 3,
        },
        {
            "description": "alternating high-low -- rob all high: 2+2=4",
            "input": [2, 1, 1, 2],
            "expected": 4,
        },
        {
            "description": "all same value -- every other house",
            "input": [5, 5, 5, 5, 5],
            "expected": 15,
        },
        {
            "description": "all zeros -- nothing to rob",
            "input": [0, 0, 0, 0],
            "expected": 0,
        },
        {
            "description": "large spike in the middle",
            "input": [1, 1, 100, 1, 1],
            "expected": 102,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = rob(list(test["input"]))
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
