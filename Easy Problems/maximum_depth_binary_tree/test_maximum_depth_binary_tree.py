import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from maximum_depth_binary_tree import max_depth, build_tree_level_order


def run_tests() -> None:
    test_cases = [
        {
            "description": "depth 3 -- right subtree is deeper",
            "values": [3, 9, 20, None, None, 15, 7],
            "expected": 3,
        },
        {
            "description": "right-skewed tree -- depth 2",
            "values": [1, None, 2],
            "expected": 2,
        },
        {
            "description": "empty tree -- depth 0",
            "values": [],
            "expected": 0,
        },
        {
            "description": "single root node -- depth 1",
            "values": [1],
            "expected": 1,
        },
        {
            "description": "perfect binary tree with 7 nodes -- depth 3",
            "values": [1, 2, 3, 4, 5, 6, 7],
            "expected": 3,
        },
        {
            "description": "left-skewed tree -- depth 4",
            "values": [1, 2, None, 3, None, None, None, 4],
            "expected": 4,
        },
        {
            "description": "two-level tree, left child only",
            "values": [1, 2],
            "expected": 2,
        },
        {
            "description": "balanced tree depth 2",
            "values": [1, 2, 3],
            "expected": 2,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        root = build_tree_level_order(test["values"])
        result = max_depth(root)
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
