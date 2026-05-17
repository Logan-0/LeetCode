import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from topKfreqElems import top_k_elements

# Note: the solution prints debug output (frequency pairs sorted ascending)
# during execution. This is expected and does not affect test results.


def run_tests() -> None:
    test_cases = [
        {
            "description": "top 2 from [1,1,1,2,2,3] -- 1 and 2",
            "numbers": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2],
        },
        {
            "description": "top 1 from [1] -- only element",
            "numbers": [1],
            "k": 1,
            "expected": [1],
        },
        {
            "description": "all elements equally frequent -- any k elements valid, check count",
            "numbers": [1, 2, 3, 4],
            "k": 2,
            "check_count_only": True,
            "expected_count": 2,
        },
        {
            "description": "top 3 from longer list -- 2, 4, 5 appear most",
            "numbers": [1, 2, 4, 2, 4, 5, 5, 4, 2, 2, 3, 5, 6, 2, 4, 3, 4, 5, 2, 4, 5, 3, 5, 4, 6, 7],
            "k": 3,
            "expected": [2, 4, 5],
        },
        {
            "description": "k equals total unique elements -- returns all",
            "numbers": [3, 1, 2],
            "k": 3,
            "expected": [1, 2, 3],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print("-- running: " + test["description"])
        result = sorted(top_k_elements(list(test["numbers"]), test["k"]))

        if test.get("check_count_only"):
            if len(result) == test["expected_count"]:
                print("PASS: " + test["description"])
                passed += 1
            else:
                print("FAIL: " + test["description"])
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
                print("  numbers:  " + str(test["numbers"]))
                print("  k:        " + str(test["k"]))
                print("  expected: " + str(expected_sorted))
                print("  got:      " + str(result))
                failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
