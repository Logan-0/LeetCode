import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from addTwoNumbers import add_two_numbers, list_to_nodes, nodes_to_list


def run_tests() -> None:
    # Digits are stored in REVERSE order in the linked list.
    # e.g. the number 342 is represented as [2, 4, 3].
    test_cases = [
        {
            "description": "342 + 465 = 807",
            "first": [2, 4, 3],
            "second": [5, 6, 4],
            "expected": [7, 0, 8],
        },
        {
            "description": "0 + 0 = 0",
            "first": [0],
            "second": [0],
            "expected": [0],
        },
        {
            "description": "single digit -- 2 + 3 = 5",
            "first": [2],
            "second": [3],
            "expected": [5],
        },
        {
            "description": "carry propagates through all digits -- 9999 + 1 = 10000",
            "first": [9, 9, 9, 9],
            "second": [1],
            "expected": [0, 0, 0, 0, 1],
        },
        {
            "description": "unequal lengths -- 100 + 99 = 199",
            "first": [0, 0, 1],
            "second": [9, 9],
            "expected": [9, 9, 1],
        },
        {
            "description": "carry on final digit -- 5 + 5 = 10",
            "first": [5],
            "second": [5],
            "expected": [0, 1],
        },
        {
            "description": "large numbers -- 9999999 + 9999 = 10009998",
            "first": [9, 9, 9, 9, 9, 9, 9],
            "second": [9, 9, 9, 9],
            "expected": [8, 9, 9, 9, 0, 0, 0, 1],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        first_head = list_to_nodes(test["first"])
        second_head = list_to_nodes(test["second"])
        result_head = add_two_numbers(first_head, second_head)
        result = nodes_to_list(result_head)
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  first:    " + str(test["first"]))
            print("  second:   " + str(test["second"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
