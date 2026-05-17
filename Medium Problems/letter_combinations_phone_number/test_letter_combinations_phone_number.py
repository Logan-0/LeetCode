import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from letterCombinationsOfAPhoneNumber import combinations_of_phone_number


def run_tests() -> None:
    test_cases = [
        {
            "description": "single digit 2 -- maps to abc",
            "input": "2",
            "expected": ["a", "b", "c"],
        },
        {
            "description": "single digit 9 -- maps to wxyz",
            "input": "9",
            "expected": ["w", "x", "y", "z"],
        },
        {
            "description": "two digits 23 -- 9 combinations",
            "input": "23",
            "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        },
        {
            "description": "digit 7 includes 4 letters (pqrs)",
            "input": "7",
            "expected": ["p", "q", "r", "s"],
        },
        {
            "description": "two digits 79 -- 4x4 = 16 combinations",
            "input": "79",
            "expected_count": 16,
            "check_count_only": True,
        },
        {
            "description": "three digits 234 -- 3x3x3 = 27 combinations",
            "input": "234",
            "expected_count": 27,
            "check_count_only": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = sorted(combinations_of_phone_number(test["input"]))

        if test.get("check_count_only"):
            if len(result) == test["expected_count"]:
                print("PASS: " + test["description"])
                passed += 1
            else:
                print("FAIL: " + test["description"])
                print("  input:          " + str(test["input"]))
                print("  expected count: " + str(test["expected_count"]))
                print("  got count:      " + str(len(result)))
                failed += 1
        else:
            expected_sorted = sorted(test["expected"])
            if result == expected_sorted:
                print("PASS: " + test["description"])
                passed += 1
            else:
                print("FAIL: " + test["description"])
                print("  input:    " + str(test["input"]))
                print("  expected: " + str(expected_sorted))
                print("  got:      " + str(result))
                failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
