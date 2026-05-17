from climbing_stairs import climb_stairs


def run_tests() -> None:
    """
    Test suite for climb_stairs.
    Runs every test case and prints PASS or FAIL with details on failures.
    """

    # The sequence of answers follows the Fibonacci pattern:
    # n=1: 1, n=2: 2, n=3: 3, n=4: 5, n=5: 8, n=6: 13, ...
    test_cases = [
        {
            "description": "1 step -- only one way: take a single step",
            "input": 1,
            "expected": 1,
        },
        {
            "description": "2 steps -- two ways: (1+1) or (2)",
            "input": 2,
            "expected": 2,
        },
        {
            "description": "3 steps -- three ways: (1+1+1), (1+2), (2+1)",
            "input": 3,
            "expected": 3,
        },
        {
            "description": "4 steps -- five ways",
            "input": 4,
            "expected": 5,
        },
        {
            "description": "5 steps -- eight ways",
            "input": 5,
            "expected": 8,
        },
        {
            "description": "6 steps -- thirteen ways",
            "input": 6,
            "expected": 13,
        },
        {
            "description": "10 steps -- eighty-nine ways",
            "input": 10,
            "expected": 89,
        },
        {
            "description": "15 steps -- 987 ways",
            "input": 15,
            "expected": 987,
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        result = climb_stairs(test_case["input"])

        if result == test_case["expected"]:
            print("PASS: " + test_case["description"])
            passed_count += 1
        else:
            print("FAIL: " + test_case["description"])
            print("  Input:    " + str(test_case["input"]) + " steps")
            print("  Expected: " + str(test_case["expected"]))
            print("  Got:      " + str(result))
            failed_count += 1

    print("")
    print("Results: " + str(passed_count) + " passed, " + str(failed_count) + " failed")


if __name__ == "__main__":
    run_tests()
