import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from longestConseqSeq import longest_consecutive_sequence

# Note: the solution prints debug output (sorted numbers and comparisons)
# during execution. This is expected and does not affect test results.


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- [1,2,3,4] is the longest sequence (length 4)",
            "input": [100, 4, 200, 1, 3, 2],
            "expected": 4,
        },
        {
            "description": "already sorted consecutive sequence",
            "input": [0, 1, 2, 3, 4],
            "expected": 5,
        },
        {
            "description": "duplicates present -- deduplicated before checking",
            "input": [1, 2, 2, 3, 4],
            "expected": 4,
        },
        {
            "description": "no consecutive numbers -- each number isolated",
            "input": [10, 20, 30, 40],
            "expected": 1,
        },
        {
            "description": "single element",
            "input": [5],
            "expected": 1,
        },
        {
            "description": "two consecutive elements",
            "input": [7, 8],
            "expected": 2,
        },
        {
            "description": "negative numbers",
            "input": [-3, -2, -1, 0, 1],
            "expected": 5,
        },
        {
            "description": "two separate sequences -- longer one wins",
            "input": [1, 2, 3, 10, 11, 12, 13],
            "expected": 4,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print("-- running: " + test["description"])
        result = longest_consecutive_sequence(list(test["input"]))
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
