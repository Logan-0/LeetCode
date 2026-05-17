import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from coinChangeDp import coin_change_dp
from coinChangeGreedy import coin_change_greedy


def run_dp_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- 11 cents with [1,2,5], minimum 3 coins",
            "coins": [1, 2, 5],
            "amount": 11,
            "expected": 3,
        },
        {
            "description": "impossible -- 3 cents with only [2] coins",
            "coins": [2],
            "amount": 3,
            "expected": -1,
        },
        {
            "description": "amount is zero -- zero coins needed",
            "coins": [1],
            "amount": 0,
            "expected": 0,
        },
        {
            "description": "single coin matches amount exactly",
            "coins": [5],
            "amount": 5,
            "expected": 1,
        },
        {
            "description": "greedy fails but DP succeeds -- [1,3,4] for 6 needs 2 coins (3+3)",
            "coins": [1, 3, 4],
            "amount": 6,
            "expected": 2,
        },
        {
            "description": "large amount with standard coins",
            "coins": [1, 5, 10, 25],
            "amount": 41,
            "expected": 4,
        },
    ]

    passed = 0
    failed = 0

    print("--- DP Approach ---")
    for test in test_cases:
        result = coin_change_dp(list(test["coins"]), test["amount"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  coins:    " + str(test["coins"]))
            print("  amount:   " + str(test["amount"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    return passed, failed


def run_greedy_tests() -> None:
    # The greedy approach works correctly when using coins that include 1
    # (guaranteeing a solution always exists) and where the greedy choice
    # happens to be optimal.
    test_cases = [
        {
            "description": "classic example -- 11 cents with [1,2,5]",
            "coins": [1, 2, 5],
            "amount": 11,
            "expected": 3,
        },
        {
            "description": "two coins -- 5+2 is optimal",
            "coins": [1, 2, 5],
            "amount": 7,
            "expected": 2,
        },
        {
            "description": "single coin fits exactly",
            "coins": [1, 5],
            "amount": 5,
            "expected": 1,
        },
        {
            "description": "only the 1-cent coin is usable",
            "coins": [1, 2, 5],
            "amount": 1,
            "expected": 1,
        },
        {
            "description": "standard US coins -- 41 cents",
            "coins": [1, 5, 10, 25],
            "amount": 41,
            "expected": 4,
        },
        {
            "description": "single denomination impossible",
            "coins": [2],
            "amount": 3,
            "expected": -1,
        },
    ]

    passed = 0
    failed = 0

    print("--- Greedy Approach ---")
    for test in test_cases:
        result = coin_change_greedy(list(test["coins"]), test["amount"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  coins:    " + str(test["coins"]))
            print("  amount:   " + str(test["amount"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    return passed, failed


def run_tests() -> None:
    dp_passed, dp_failed = run_dp_tests()
    gr_passed, gr_failed = run_greedy_tests()
    total_passed = dp_passed + gr_passed
    total_failed = dp_failed + gr_failed
    print("\nResults: " + str(total_passed) + " passed, " + str(total_failed) + " failed")


if __name__ == "__main__":
    run_tests()
