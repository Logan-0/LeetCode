from valid_parentheses import is_valid


def run_tests() -> None:
    """
    Test suite for is_valid.
    Runs every test case and prints PASS or FAIL with details on failures.
    """

    test_cases = [
        {
            "description": "single pair of parentheses",
            "input": "()",
            "expected": True,
        },
        {
            "description": "three different bracket types in sequence",
            "input": "()[]{}",
            "expected": True,
        },
        {
            "description": "mismatched bracket types",
            "input": "(]",
            "expected": False,
        },
        {
            "description": "interleaved brackets -- invalid nesting order",
            "input": "([)]",
            "expected": False,
        },
        {
            "description": "curly brace containing square brackets -- valid nesting",
            "input": "{[]}",
            "expected": True,
        },
        {
            "description": "empty string is considered valid",
            "input": "",
            "expected": True,
        },
        {
            "description": "single unclosed opening bracket",
            "input": "(",
            "expected": False,
        },
        {
            "description": "single closing bracket with no matching opener",
            "input": "]",
            "expected": False,
        },
        {
            "description": "deeply nested parentheses",
            "input": "((()))",
            "expected": True,
        },
        {
            "description": "complex valid nesting of all three types",
            "input": "({[]})",
            "expected": True,
        },
        {
            "description": "extra closing bracket after a valid pair",
            "input": "())",
            "expected": False,
        },
        {
            "description": "multiple pairs, one mismatched at the end",
            "input": "()[{}(])",
            "expected": False,
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        result = is_valid(test_case["input"])

        if result == test_case["expected"]:
            print("PASS: " + test_case["description"])
            passed_count += 1
        else:
            print("FAIL: " + test_case["description"])
            print("  Input:    '" + test_case["input"] + "'")
            print("  Expected: " + str(test_case["expected"]))
            print("  Got:      " + str(result))
            failed_count += 1

    print("")
    print("Results: " + str(passed_count) + " passed, " + str(failed_count) + " failed")


if __name__ == "__main__":
    run_tests()
