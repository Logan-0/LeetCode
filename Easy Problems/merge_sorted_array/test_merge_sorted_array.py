import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from mergeSortedArray import merge_sorted_array


def run_tests() -> None:
    # The first array must have trailing zeros to hold the second array's elements.
    # The function merges in place and returns the modified first array.
    test_cases = [
        {
            "description": "main example -- [1,3,4,5] merged with [2,4,7]",
            "first": [1, 3, 4, 5, 0, 0, 0],
            "m": 4,
            "second": [2, 4, 7],
            "n": 3,
            "expected": [1, 2, 3, 4, 4, 5, 7],
        },
        {
            "description": "standard merge -- interleaved values",
            "first": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "second": [2, 5, 6],
            "n": 3,
            "expected": [1, 2, 2, 3, 5, 6],
        },
        {
            "description": "second array all larger",
            "first": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "second": [4, 5, 6],
            "n": 3,
            "expected": [1, 2, 3, 4, 5, 6],
        },
        {
            "description": "second array all smaller",
            "first": [4, 5, 6, 0, 0, 0],
            "m": 3,
            "second": [1, 2, 3],
            "n": 3,
            "expected": [1, 2, 3, 4, 5, 6],
        },
        {
            "description": "first array is empty -- only second array values",
            "first": [0],
            "m": 0,
            "second": [1],
            "n": 1,
            "expected": [1],
        },
        {
            "description": "second array is empty -- first stays unchanged",
            "first": [1],
            "m": 1,
            "second": [],
            "n": 0,
            "expected": [1],
        },
        {
            "description": "single elements -- smaller goes first",
            "first": [2, 0],
            "m": 1,
            "second": [1],
            "n": 1,
            "expected": [1, 2],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = merge_sorted_array(
            list(test["first"]), test["m"], list(test["second"]), test["n"]
        )
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  first:    " + str(test["first"]) + " (m=" + str(test["m"]) + ")")
            print("  second:   " + str(test["second"]) + " (n=" + str(test["n"]) + ")")
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
