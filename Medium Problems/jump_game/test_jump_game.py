import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from jump_game import can_jump


def run_tests() -> None:
    test_cases = [
        {
            "description": "reachable -- can jump over the zeros",
            "input": [2, 3, 1, 1, 4],
            "expected": True,
        },
        {
            "description": "not reachable -- stuck at the zero",
            "input": [3, 2, 1, 0, 4],
            "expected": False,
        },
        {
            "description": "single element -- already at last index",
            "input": [0],
            "expected": True,
        },
        {
            "description": "jump over a zero to reach the end",
            "input": [2, 0, 0],
            "expected": True,
        },
        {
            "description": "zero blocks progress after one step",
            "input": [1, 0, 1, 0],
            "expected": False,
        },
        {
            "description": "all ones -- always reachable",
            "input": [1, 1, 1, 1, 1],
            "expected": True,
        },
        {
            "description": "first element large enough to jump to end",
            "input": [5, 0, 0, 0, 0],
            "expected": True,
        },
        {
            "description": "two elements, jump of 1 reaches end",
            "input": [1, 0],
            "expected": True,
        },
        {
            "description": "zero at start with two elements",
            "input": [0, 1],
            "expected": False,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = can_jump(test["input"])
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
