import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from twoSumBruteForce import two_sum_brute_force
from twoSumOnePassHash import two_sum_one_pass_hash


def run_brute_force_tests() -> None:
    test_cases = [
        {
            "description": "basic example -- indices 2 and 5 sum to 45",
            "numbers": [4, 5, 3, 67, 13, 42, 15],
            "target": 45,
            "expected": [2, 5],
        },
        {
            "description": "target at the start of the list",
            "numbers": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1],
        },
        {
            "description": "target at the end of the list",
            "numbers": [3, 2, 4],
            "target": 6,
            "expected": [1, 2],
        },
        {
            "description": "same number used twice",
            "numbers": [3, 3],
            "target": 6,
            "expected": [0, 1],
        },
        {
            "description": "no valid pair -- returns empty list",
            "numbers": [1, 2, 3],
            "target": 10,
            "expected": [],
        },
        {
            "description": "negative numbers",
            "numbers": [-1, -2, -3, -4, -5],
            "target": -8,
            "expected": [2, 4],
        },
    ]

    passed = 0
    failed = 0

    print("--- Brute Force ---")
    for test in test_cases:
        result = two_sum_brute_force(test["numbers"], test["target"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  numbers:  " + str(test["numbers"]))
            print("  target:   " + str(test["target"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    return passed, failed


def run_one_pass_hash_tests() -> None:
    test_cases = [
        {
            "description": "basic example -- indices 2 and 5 sum to 45",
            "numbers": [4, 5, 3, 67, 13, 42, 15],
            "target": 45,
            "expected": [2, 5],
        },
        {
            "description": "target at the start of the list",
            "numbers": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1],
        },
        {
            "description": "target at the end of the list",
            "numbers": [3, 2, 4],
            "target": 6,
            "expected": [1, 2],
        },
        {
            "description": "same number used twice",
            "numbers": [3, 3],
            "target": 6,
            "expected": [0, 1],
        },
        {
            "description": "no valid pair -- returns empty list",
            "numbers": [1, 2, 3],
            "target": 10,
            "expected": [],
        },
        {
            "description": "negative numbers",
            "numbers": [-1, -2, -3, -4, -5],
            "target": -8,
            "expected": [2, 4],
        },
    ]

    passed = 0
    failed = 0

    print("--- One Pass Hash ---")
    for test in test_cases:
        result = two_sum_one_pass_hash(test["numbers"], test["target"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  numbers:  " + str(test["numbers"]))
            print("  target:   " + str(test["target"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    return passed, failed


def run_tests() -> None:
    bf_passed, bf_failed = run_brute_force_tests()
    oph_passed, oph_failed = run_one_pass_hash_tests()
    total_passed = bf_passed + oph_passed
    total_failed = bf_failed + oph_failed
    print("\nResults: " + str(total_passed) + " passed, " + str(total_failed) + " failed")


if __name__ == "__main__":
    run_tests()
