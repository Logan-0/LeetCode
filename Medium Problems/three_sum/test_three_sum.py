from three_sum import three_sum


def normalize_triplets(triplets: list[list[int]]) -> list[list[int]]:
    """
    Sorts each triplet and then sorts the list of triplets.
    This makes comparison order-independent so tests do not depend on
    the order in which our algorithm discovers triplets.
    """
    return sorted([sorted(triplet) for triplet in triplets])


def run_tests() -> None:
    """
    Test suite for three_sum.
    Runs every test case and prints PASS or FAIL with details on failures.

    Because the problem allows any valid ordering of the output triplets,
    we normalize both the result and the expected value before comparing.
    """

    test_cases = [
        {
            "description": "classic example -- two triplets",
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]],
        },
        {
            "description": "no triplet sums to zero",
            "input": [0, 1, 1],
            "expected": [],
        },
        {
            "description": "all zeros -- one triplet of three zeros",
            "input": [0, 0, 0],
            "expected": [[0, 0, 0]],
        },
        {
            "description": "mixed negatives and positives -- two triplets",
            "input": [-2, 0, 1, 1, 2],
            "expected": [[-2, 0, 2], [-2, 1, 1]],
        },
        {
            "description": "empty list -- no triplets possible",
            "input": [],
            "expected": [],
        },
        {
            "description": "fewer than three elements -- no triplets possible",
            "input": [1, 2],
            "expected": [],
        },
        {
            "description": "all positive values -- no triplet can sum to zero",
            "input": [1, 2, 3, 4, 5],
            "expected": [],
        },
        {
            "description": "many duplicates -- should return only unique triplets",
            "input": [-2, -2, 0, 0, 2, 2],
            "expected": [[-2, 0, 2]],
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        result = three_sum(test_case["input"])
        normalized_result = normalize_triplets(result)
        normalized_expected = normalize_triplets(test_case["expected"])

        if normalized_result == normalized_expected:
            print("PASS: " + test_case["description"])
            passed_count += 1
        else:
            print("FAIL: " + test_case["description"])
            print("  Input:    " + str(test_case["input"]))
            print("  Expected: " + str(normalized_expected))
            print("  Got:      " + str(normalized_result))
            failed_count += 1

    print("")
    print("Results: " + str(passed_count) + " passed, " + str(failed_count) + " failed")


if __name__ == "__main__":
    run_tests()
