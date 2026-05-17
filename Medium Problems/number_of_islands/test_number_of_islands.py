import sys
import os
import copy
sys.path.insert(0, os.path.dirname(__file__))

from numberOfIslands import num_of_islands


def run_tests() -> None:
    # Note: num_of_islands modifies the grid in place (marks visited land as water).
    # Each test uses copy.deepcopy to preserve the original for display on failure.
    test_cases = [
        {
            "description": "one large connected island",
            "grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            "expected": 1,
        },
        {
            "description": "three separate islands",
            "grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            "expected": 3,
        },
        {
            "description": "all water -- no islands",
            "grid": [
                ["0", "0", "0"],
                ["0", "0", "0"],
            ],
            "expected": 0,
        },
        {
            "description": "all land -- one giant island",
            "grid": [
                ["1", "1"],
                ["1", "1"],
            ],
            "expected": 1,
        },
        {
            "description": "single land cell",
            "grid": [["1"]],
            "expected": 1,
        },
        {
            "description": "single water cell",
            "grid": [["0"]],
            "expected": 0,
        },
        {
            "description": "diagonal cells are NOT connected -- four islands",
            "grid": [
                ["1", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "1"],
            ],
            "expected": 5,
        },
        {
            "description": "single row -- each land segment is its own island",
            "grid": [["1", "0", "1", "0", "1"]],
            "expected": 3,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        grid_copy = copy.deepcopy(test["grid"])
        result = num_of_islands(grid_copy)
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
