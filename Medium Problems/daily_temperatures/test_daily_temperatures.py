import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from dailyTemperatures import daily_temperatures
from dailyTemperaturesStack import daily_temperatures_stack


def build_test_cases() -> list:
    return [
        {
            "description": "classic LeetCode example",
            "input": [73, 74, 75, 71, 69, 72, 76, 73],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0],
        },
        {
            "description": "monotonically decreasing -- no warmer day for any",
            "input": [100, 90, 80, 70],
            "expected": [0, 0, 0, 0],
        },
        {
            "description": "monotonically increasing -- each day waits one day",
            "input": [30, 40, 50, 60],
            "expected": [1, 1, 1, 0],
        },
        {
            "description": "all same temperatures -- no warmer day",
            "input": [50, 50, 50, 50],
            "expected": [0, 0, 0, 0],
        },
        {
            "description": "single day -- no future days",
            "input": [72],
            "expected": [0],
        },
        {
            "description": "two days -- warmer tomorrow",
            "input": [60, 61],
            "expected": [1, 0],
        },
        {
            "description": "two days -- colder tomorrow",
            "input": [61, 60],
            "expected": [0, 0],
        },
        {
            "description": "warmer day is far away",
            "input": [55, 54, 53, 52, 56],
            "expected": [4, 3, 2, 1, 0],
        },
    ]


def run_tests() -> None:
    test_cases = build_test_cases()
    passed = 0
    failed = 0

    print("--- Hash Map Approach ---")
    for test in test_cases:
        result = daily_temperatures(list(test["input"]))
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  input:    " + str(test["input"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("--- Monotonic Stack Approach ---")
    for test in test_cases:
        result = daily_temperatures_stack(list(test["input"]))
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
