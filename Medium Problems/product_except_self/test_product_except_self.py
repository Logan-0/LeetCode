from product_except_self import product_except_self


def run_tests() -> None:
    """
    Test suite for product_except_self.
    Runs every test case and prints PASS or FAIL with details on failures.
    """

    test_cases = [
        {
            "description": "basic four-element example from the problem description",
            "input": [1, 2, 3, 4],
            "expected": [24, 12, 8, 6],
        },
        {
            "description": "list containing a zero -- every product that includes the zero slot is 0",
            "input": [-1, 1, 0, -3, 3],
            "expected": [0, 0, 9, 0, 0],
        },
        {
            "description": "list with two zeros -- all products become 0",
            "input": [0, 0, 1, 2],
            "expected": [0, 0, 0, 0],
        },
        {
            "description": "two-element list",
            "input": [3, 7],
            "expected": [7, 3],
        },
        {
            "description": "all ones -- every product is 1",
            "input": [1, 1, 1, 1],
            "expected": [1, 1, 1, 1],
        },
        {
            "description": "list with negative numbers",
            "input": [-2, -3, 4],
            "expected": [-12, -8, 6],
        },
        {
            "description": "single-element list -- the only product (of an empty set) is 1",
            "input": [5],
            "expected": [1],
        },
        {
            "description": "all same values",
            "input": [2, 2, 2, 2],
            "expected": [8, 8, 8, 8],
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        result = product_except_self(test_case["input"])

        if result == test_case["expected"]:
            print("PASS: " + test_case["description"])
            passed_count += 1
        else:
            print("FAIL: " + test_case["description"])
            print("  Input:    " + str(test_case["input"]))
            print("  Expected: " + str(test_case["expected"]))
            print("  Got:      " + str(result))
            failed_count += 1

    print("")
    print("Results: " + str(passed_count) + " passed, " + str(failed_count) + " failed")


if __name__ == "__main__":
    run_tests()
