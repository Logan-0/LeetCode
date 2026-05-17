from reverse_linked_list import list_to_nodes, nodes_to_list, reverse_linked_list


def run_tests() -> None:
    """
    Test suite for reverse_linked_list.
    Runs every test case and prints PASS or FAIL with details on failures.

    Each test builds a fresh linked list from a Python list, reverses it,
    converts the result back to a Python list, then compares.
    """

    test_cases = [
        {
            "description": "five-element list reversed",
            "input": [1, 2, 3, 4, 5],
            "expected": [5, 4, 3, 2, 1],
        },
        {
            "description": "two-element list reversed",
            "input": [1, 2],
            "expected": [2, 1],
        },
        {
            "description": "single-element list -- reversing changes nothing",
            "input": [42],
            "expected": [42],
        },
        {
            "description": "empty list -- reversing returns empty",
            "input": [],
            "expected": [],
        },
        {
            "description": "list with negative values",
            "input": [-3, -2, -1, 0, 1],
            "expected": [1, 0, -1, -2, -3],
        },
        {
            "description": "list with duplicate values",
            "input": [1, 1, 2, 2, 3],
            "expected": [3, 2, 2, 1, 1],
        },
        {
            "description": "reversing twice returns the original order",
            "input": [10, 20, 30],
            "expected": [10, 20, 30],
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        head = list_to_nodes(test_case["input"])

        # Special handling for the double-reverse test
        if test_case["description"] == "reversing twice returns the original order":
            head = reverse_linked_list(head)
            head = reverse_linked_list(head)
        else:
            head = reverse_linked_list(head)

        result = nodes_to_list(head)

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
