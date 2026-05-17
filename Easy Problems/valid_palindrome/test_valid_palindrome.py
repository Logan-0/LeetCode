import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from valid_palindrome import is_palindrome


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic palindrome sentence with punctuation",
            "input": "A man, a plan, a canal: Panama",
            "expected": True,
        },
        {
            "description": "not a palindrome",
            "input": "race a car",
            "expected": False,
        },
        {
            "description": "single space -- empty after filtering, counts as palindrome",
            "input": " ",
            "expected": True,
        },
        {
            "description": "palindrome with mixed punctuation",
            "input": "No 'x' in Nixon",
            "expected": True,
        },
        {
            "description": "palindrome phrase with question mark",
            "input": "Was it a car or a cat I saw?",
            "expected": True,
        },
        {
            "description": "digits in the string",
            "input": "A1B2B1A",
            "expected": True,
        },
        {
            "description": "only letters, simple palindrome",
            "input": "racecar",
            "expected": True,
        },
        {
            "description": "only letters, not a palindrome",
            "input": "hello",
            "expected": False,
        },
        {
            "description": "single alphanumeric character",
            "input": "a",
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = is_palindrome(test["input"])
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
