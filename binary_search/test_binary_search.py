from binary_search import binary_search


def run_tests() -> None:
    """
    Test suite for binary_search.
    Runs every test case and prints PASS or FAIL with details on failures.
    """

    sorted_list = [-10, -3, 0, 5, 9, 14, 22, 35, 47]

    test_cases = [
        {
            "description": "target found in the middle of the list",
            "numbers": sorted_list,
            "target": 9,
            "expected": 4,
        },
        {
            "description": "target found at the very first index",
            "numbers": sorted_list,
            "target": -10,
            "expected": 0,
        },
        {
            "description": "target found at the very last index",
            "numbers": sorted_list,
            "target": 47,
            "expected": 8,
        },
        {
            "description": "target found at index 1 (negative number)",
            "numbers": sorted_list,
            "target": -3,
            "expected": 1,
        },
        {
            "description": "target greater than all elements -- not found",
            "numbers": sorted_list,
            "target": 100,
            "expected": -1,
        },
        {
            "description": "target less than all elements -- not found",
            "numbers": sorted_list,
            "target": -99,
            "expected": -1,
        },
        {
            "description": "target between two elements but not present -- not found",
            "numbers": sorted_list,
            "target": 1,
            "expected": -1,
        },
        {
            "description": "single-element list, target matches",
            "numbers": [42],
            "target": 42,
            "expected": 0,
        },
        {
            "description": "single-element list, target does not match",
            "numbers": [42],
            "target": 7,
            "expected": -1,
        },
        {
            "description": "empty list always returns not found",
            "numbers": [],
            "target": 5,
            "expected": -1,
        },
        {
            "description": "two-element list, target is the second element",
            "numbers": [3, 7],
            "target": 7,
            "expected": 1,
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        result = binary_search(test_case["numbers"], test_case["target"])

        if result == test_case["expected"]:
            print("PASS: " + test_case["description"])
            passed_count += 1
        else:
            print("FAIL: " + test_case["description"])
            print("  Numbers: " + str(test_case["numbers"]))
            print("  Target:  " + str(test_case["target"]))
            print("  Expected index: " + str(test_case["expected"]))
            print("  Got index:      " + str(result))
            failed_count += 1

    print("")
    print("Results: " + str(passed_count) + " passed, " + str(failed_count) + " failed")


if __name__ == "__main__":
    run_tests()
