import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from finalPricesWithDiscount import final_prices


def run_tests() -> None:
    # Note: final_prices modifies the input list in place.
    # Each test case passes a fresh list to avoid interference.
    test_cases = [
        {
            "description": "example from the problem -- [8,4,6,2,3] -> [4,2,4,2,3]",
            "input": [8, 4, 6, 2, 3],
            "expected": [4, 2, 4, 2, 3],
        },
        {
            "description": "monotonically increasing -- no discounts applied",
            "input": [1, 2, 3, 4, 5],
            "expected": [1, 2, 3, 4, 5],
        },
        {
            "description": "monotonically decreasing -- each item discounted by the next",
            "input": [5, 4, 3, 2, 1],
            "expected": [1, 1, 1, 1, 1],
        },
        {
            "description": "single item -- no discount possible",
            "input": [10],
            "expected": [10],
        },
        {
            "description": "all same price -- each discounted to 0 except the last",
            "input": [5, 5, 5, 5],
            "expected": [0, 0, 0, 5],
        },
        {
            "description": "discount skips over higher prices to find first lower or equal",
            "input": [10, 15, 8, 20],
            "expected": [2, 7, 8, 20],
        },
        {
            "description": "two items -- first discounted by second",
            "input": [3, 2],
            "expected": [1, 2],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = final_prices(list(test["input"]))
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
