import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from lengthOfLongestSubstring import length_of_longest_substring
from lengthOfLongestSubstringSlidingWindow import length_of_longest_substring_sliding_window


def build_test_cases() -> list:
    return [
        {
            "description": "classic example -- 'abc' is the longest unique substring",
            "input": "abcabcbb",
            "expected": 3,
        },
        {
            "description": "all same characters -- length 1",
            "input": "bbbbb",
            "expected": 1,
        },
        {
            "description": "repeat near the end -- 'wke' has length 3",
            "input": "pwwkew",
            "expected": 3,
        },
        {
            "description": "empty string -- length 0",
            "input": "",
            "expected": 0,
        },
        {
            "description": "single character",
            "input": "a",
            "expected": 1,
        },
        {
            "description": "all unique characters -- entire string",
            "input": "abcdef",
            "expected": 6,
        },
        {
            "description": "two characters alternating",
            "input": "ababab",
            "expected": 2,
        },
        {
            "description": "longer string with unique window in the middle",
            "input": "aabcdeaa",
            "expected": 5,
        },
    ]


def run_tests() -> None:
    test_cases = build_test_cases()
    passed = 0
    failed = 0

    print("--- Brute Force Approach ---")
    for test in test_cases:
        result = length_of_longest_substring(test["input"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  input:    " + str(test["input"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("--- Sliding Window Approach ---")
    for test in test_cases:
        result = length_of_longest_substring_sliding_window(test["input"])
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
