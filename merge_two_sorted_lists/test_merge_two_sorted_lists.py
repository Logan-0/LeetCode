import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from mergeTwoSortedLinkedLists import merge_two_lists, list_to_nodes, nodes_to_list


def run_tests() -> None:
    test_cases = [
        {
            "description": "interleaved values -- [1,2,4] + [1,3,4] = [1,1,2,3,4,4]",
            "first": [1, 2, 4],
            "second": [1, 3, 4],
            "expected": [1, 1, 2, 3, 4, 4],
        },
        {
            "description": "both lists empty",
            "first": [],
            "second": [],
            "expected": [],
        },
        {
            "description": "first list empty -- second list returned",
            "first": [],
            "second": [1, 2, 3],
            "expected": [1, 2, 3],
        },
        {
            "description": "second list empty -- first list returned",
            "first": [1, 2, 3],
            "second": [],
            "expected": [1, 2, 3],
        },
        {
            "description": "second list entirely larger",
            "first": [1, 2, 3],
            "second": [4, 5, 6],
            "expected": [1, 2, 3, 4, 5, 6],
        },
        {
            "description": "first list entirely larger",
            "first": [4, 5, 6],
            "second": [1, 2, 3],
            "expected": [1, 2, 3, 4, 5, 6],
        },
        {
            "description": "single elements -- smaller first",
            "first": [5],
            "second": [3],
            "expected": [3, 5],
        },
        {
            "description": "unequal lengths",
            "first": [1, 3, 5, 7],
            "second": [2, 4],
            "expected": [1, 2, 3, 4, 5, 7],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        first_head = list_to_nodes(test["first"])
        second_head = list_to_nodes(test["second"])
        result_head = merge_two_lists(first_head, second_head)
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
