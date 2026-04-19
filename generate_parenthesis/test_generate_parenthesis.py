import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from generateParenthesis import generate_parenthesis


def run_tests() -> None:
    test_cases = [
        {
            "description": "1 pair -- only one valid combination",
            "input": 1,
            "expected": ["()"],
        },
        {
            "description": "2 pairs -- two valid combinations",
            "input": 2,
            "expected": ["(())", "()()"],
        },
        {
            "description": "3 pairs -- five valid combinations (Catalan number C(3)=5)",
            "input": 3,
            "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"],
        },
        {
            "description": "4 pairs -- fourteen valid combinations (Catalan number C(4)=14)",
            "input": 4,
            "expected_count": 14,
            "check_count_only": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = sorted(generate_parenthesis(test["input"]))

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
