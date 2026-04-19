import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from longestIncSubseq import length_of_lis

# Note: the solution prints debug output (DP extension steps)
# during execution. This is expected and does not affect test results.


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- LIS is [1,4,6,13,20] or [1,2,3,13,20], length 5",
            "input": [1, 4, 2, 6, 3, 13, 20],
            "expected": 5,
        },
        {
            "description": "already sorted -- entire array is the LIS",
            "input": [1, 2, 3, 4, 5],
            "expected": 5,
        },
        {
            "description": "reverse sorted -- each element is its own subsequence, length 1",
            "input": [5, 4, 3, 2, 1],
            "expected": 1,
        },
        {
            "description": "single element",
            "input": [42],
            "expected": 1,
        },
        {
            "description": "all same elements -- LIS length 1",
            "input": [7, 7, 7, 7],
            "expected": 1,
        },
        {
            "description": "two elements increasing",
            "input": [1, 2],
            "expected": 2,
        },
        {
            "description": "two elements decreasing",
            "input": [2, 1],
            "expected": 1,
        },
        {
            "description": "mixed with multiple valid LIS paths",
            "input": [3, 10, 2, 1, 20],
            "expected": 3,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print("-- running: " + test["description"])
        result = length_of_lis(list(test["input"]))
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
