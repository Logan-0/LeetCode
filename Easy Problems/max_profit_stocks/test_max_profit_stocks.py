import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from maxProfitStocks import max_profit


def run_tests() -> None:
    test_cases = [
        {
            "description": "main example -- multiple transactions total 16",
            "input": [1, 6, 4, 7, 3, 1, 2, 4, 5, 9, 0],
            "expected": 16,
        },
        {
            "description": "monotonically increasing -- buy once and hold",
            "input": [1, 2, 3, 4, 5],
            "expected": 4,
        },
        {
            "description": "monotonically decreasing -- no profitable trade",
            "input": [5, 4, 3, 2, 1],
            "expected": 0,
        },
        {
            "description": "single day -- no transactions possible",
            "input": [10],
            "expected": 0,
        },
        {
            "description": "all same price -- no profit",
            "input": [5, 5, 5, 5],
            "expected": 0,
        },
        {
            "description": "alternating up and down -- capture every rise",
            "input": [1, 2, 1, 2, 1, 2],
            "expected": 3,
        },
        {
            "description": "two days -- one profitable transaction",
            "input": [3, 8],
            "expected": 5,
        },
        {
            "description": "two days -- no profit (price dropped)",
            "input": [8, 3],
            "expected": 0,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = max_profit(list(test["input"]))
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
