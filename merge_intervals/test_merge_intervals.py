import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from mergeIntervals import merge_intervals


def run_tests() -> None:
    test_cases = [
        {
            "description": "overlapping intervals merge, non-overlapping stay",
            "input": [[1, 3], [2, 5], [6, 7], [9, 14], [10, 15]],
            "expected": [[1, 5], [6, 7], [9, 15]],
        },
        {
            "description": "no overlapping intervals -- returned unchanged",
            "input": [[1, 2], [4, 5], [7, 8]],
            "expected": [[1, 2], [4, 5], [7, 8]],
        },
        {
            "description": "all intervals merge into one",
            "input": [[1, 4], [2, 5], [3, 6]],
            "expected": [[1, 6]],
        },
        {
            "description": "single interval -- returned as is",
            "input": [[1, 5]],
            "expected": [[1, 5]],
        },
        {
            "description": "touching but not overlapping boundaries -- treated as non-overlapping",
            "input": [[1, 3], [4, 6]],
            "expected": [[1, 3], [4, 6]],
        },
        {
            "description": "one interval fully contains another",
            "input": [[1, 10], [2, 6]],
            "expected": [[1, 10]],
        },
        {
            "description": "unsorted input -- function sorts before merging",
            "input": [[15, 18], [1, 3], [8, 10], [2, 6]],
            "expected": [[1, 6], [8, 10], [15, 18]],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = merge_intervals([list(interval) for interval in test["input"]])
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
