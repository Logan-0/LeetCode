import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from contains_duplicate import contains_duplicate


def run_tests() -> None:
    test_cases = [
        {
            "description": "duplicate exists -- 1 appears twice",
            "input": [1, 2, 3, 1],
            "expected": True,
        },
        {
            "description": "all distinct -- no duplicates",
            "input": [1, 2, 3, 4],
            "expected": False,
        },
        {
            "description": "multiple duplicates",
            "input": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            "expected": True,
        },
        {
            "description": "single element -- cannot have duplicate",
            "input": [5],
            "expected": False,
        },
        {
            "description": "two identical elements",
            "input": [7, 7],
            "expected": True,
        },
        {
            "description": "two different elements",
            "input": [7, 8],
            "expected": False,
        },
        {
            "description": "large range with one duplicate",
            "input": list(range(100)) + [42],
            "expected": True,
        },
        {
            "description": "large range all distinct",
            "input": list(range(100)),
            "expected": False,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = contains_duplicate(test["input"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  input:    " + str(test["input"][:10]) + ("..." if len(test["input"]) > 10 else ""))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
