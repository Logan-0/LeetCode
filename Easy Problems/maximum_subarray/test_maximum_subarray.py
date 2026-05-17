import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from maximum_subarray import max_subarray


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- subarray [4,-1,2,1] sums to 6",
            "input": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            "expected": 6,
        },
        {
            "description": "single element",
            "input": [1],
            "expected": 1,
        },
        {
            "description": "all positive -- take the whole array",
            "input": [5, 4, -1, 7, 8],
            "expected": 23,
        },
        {
            "description": "all negative -- take the least negative single element",
            "input": [-1, -2, -3, -4],
            "expected": -1,
        },
        {
            "description": "all same positive number",
            "input": [3, 3, 3, 3],
            "expected": 12,
        },
        {
            "description": "single negative element",
            "input": [-5],
            "expected": -5,
        },
        {
            "description": "large dip then recovery",
            "input": [8, -100, 5, 6, 7],
            "expected": 18,
        },
        {
            "description": "best subarray is at the end",
            "input": [-5, -3, 1, 2, 3],
            "expected": 6,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = max_subarray(test["input"])
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
