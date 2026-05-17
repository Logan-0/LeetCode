import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from countCompleteTreeNodes import count_complete_tree_nodes, build_tree_level_order


def run_tests() -> None:
    test_cases = [
        {
            "description": "empty tree -- 0 nodes",
            "values": [],
            "expected": 0,
        },
        {
            "description": "single node",
            "values": [1],
            "expected": 1,
        },
        {
            "description": "perfect binary tree with 3 nodes",
            "values": [1, 2, 3],
            "expected": 3,
        },
        {
            "description": "perfect binary tree with 7 nodes",
            "values": [1, 2, 3, 4, 5, 6, 7],
            "expected": 7,
        },
        {
            "description": "incomplete level -- 5 nodes",
            "values": [1, 2, 3, 4, 5],
            "expected": 5,
        },
        {
            "description": "tree with 10 nodes from the main example",
            "values": [1, 4, 6, 3, 66, 23, 54, 11, 90, 84],
            "expected": 10,
        },
        {
            "description": "left-skewed tree -- 4 nodes",
            "values": [1, 2, None, 3, None, None, None, 4],
            "expected": 4,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        root = build_tree_level_order(test["values"])
        result = count_complete_tree_nodes(root)
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  values:   " + str(test["values"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
