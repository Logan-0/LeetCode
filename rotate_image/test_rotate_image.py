import copy

from rotate_image import rotate_image


def run_tests() -> None:
    """
    Test suite for rotate_image.
    Runs every test case and prints PASS or FAIL with details on failures.

    Because rotate_image modifies the matrix in place, we deep-copy the
    input before passing it so each test case stays independent.
    """

    test_cases = [
        {
            "description": "3x3 matrix -- standard example",
            "input": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            "expected": [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
            ],
        },
        {
            "description": "4x4 matrix",
            "input": [
                [ 5,  1,  9, 11],
                [ 2,  4,  8, 10],
                [13,  3,  6,  7],
                [15, 14, 12, 16],
            ],
            "expected": [
                [15, 13,  2,  5],
                [14,  3,  4,  1],
                [12,  6,  8,  9],
                [16,  7, 10, 11],
            ],
        },
        {
            "description": "1x1 matrix -- rotation changes nothing",
            "input": [[42]],
            "expected": [[42]],
        },
        {
            "description": "2x2 matrix",
            "input": [
                [1, 2],
                [3, 4],
            ],
            "expected": [
                [3, 1],
                [4, 2],
            ],
        },
        {
            "description": "3x3 matrix of all zeros -- rotation changes nothing",
            "input": [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            "expected": [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
        },
        {
            "description": "3x3 identity-like matrix rotated four times returns to original",
            "input": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            "expected": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            "rotate_times": 4,
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        # Deep copy so the original test data is not modified
        matrix_copy = copy.deepcopy(test_case["input"])

        rotate_count = test_case.get("rotate_times", 1)
        for _ in range(rotate_count):
            rotate_image(matrix_copy)

        if matrix_copy == test_case["expected"]:
            print("PASS: " + test_case["description"])
            passed_count += 1
        else:
            print("FAIL: " + test_case["description"])
            print("  Input:")
            for row in test_case["input"]:
                print("    " + str(row))
            print("  Expected:")
            for row in test_case["expected"]:
                print("    " + str(row))
            print("  Got:")
            for row in matrix_copy:
                print("    " + str(row))
            failed_count += 1

    print("")
    print("Results: " + str(passed_count) + " passed, " + str(failed_count) + " failed")


if __name__ == "__main__":
    run_tests()
