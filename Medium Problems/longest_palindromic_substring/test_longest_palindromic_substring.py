from longest_palindromic_substring import longest_palindromic_substring


def is_palindrome(text: str) -> bool:
    """Returns True if text reads the same forwards and backwards."""
    return text == text[::-1]


def run_tests() -> None:
    """
    Test suite for longest_palindromic_substring.
    Runs every test case and prints PASS or FAIL with details on failures.

    Some inputs have multiple equally valid answers (e.g., "babad" can
    return either "bab" or "aba"). For those cases we check two things:
      1. The returned string is actually a palindrome
      2. The returned string has the expected length

    For inputs with a single unambiguous answer we check the exact string.
    """

    test_cases = [
        {
            "description": "classic example -- 'bab' and 'aba' both valid, check length 3",
            "input": "babad",
            "check_exact": False,
            "expected_length": 3,
            "expected": None,
        },
        {
            "description": "even-length palindrome 'bb'",
            "input": "cbbd",
            "check_exact": True,
            "expected_length": 2,
            "expected": "bb",
        },
        {
            "description": "entire string is a palindrome",
            "input": "racecar",
            "check_exact": True,
            "expected_length": 7,
            "expected": "racecar",
        },
        {
            "description": "entire string is a palindrome (odd length)",
            "input": "abacaba",
            "check_exact": True,
            "expected_length": 7,
            "expected": "abacaba",
        },
        {
            "description": "single character -- always a palindrome",
            "input": "a",
            "check_exact": True,
            "expected_length": 1,
            "expected": "a",
        },
        {
            "description": "two different characters -- first character returned",
            "input": "ac",
            "check_exact": True,
            "expected_length": 1,
            "expected": "a",
        },
        {
            "description": "two identical characters -- both form a palindrome",
            "input": "aa",
            "check_exact": True,
            "expected_length": 2,
            "expected": "aa",
        },
        {
            "description": "palindrome embedded in the middle of a longer string",
            "input": "xabcbay",
            "check_exact": False,
            "expected_length": 5,
            "expected": None,
        },
        {
            "description": "all same characters -- entire string is the answer",
            "input": "aaaa",
            "check_exact": True,
            "expected_length": 4,
            "expected": "aaaa",
        },
        {
            "description": "no repeated characters -- single character returned",
            "input": "abcde",
            "check_exact": False,
            "expected_length": 1,
            "expected": None,
        },
    ]

    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        result = longest_palindromic_substring(test_case["input"])

        result_is_palindrome = is_palindrome(result)
        result_has_correct_length = len(result) == test_case["expected_length"]

        if test_case["check_exact"]:
            passed = (result == test_case["expected"])
        else:
            passed = result_is_palindrome and result_has_correct_length

        if passed:
            print("PASS: " + test_case["description"])
            passed_count += 1
        else:
            print("FAIL: " + test_case["description"])
            print("  Input:            '" + test_case["input"] + "'")
            print("  Expected length:  " + str(test_case["expected_length"]))
            if test_case["check_exact"]:
                print("  Expected:         '" + str(test_case["expected"]) + "'")
            print("  Got:              '" + result + "'")
            print("  Is palindrome:    " + str(result_is_palindrome))
            print("  Length correct:   " + str(result_has_correct_length))
            failed_count += 1

    print("")
    print("Results: " + str(passed_count) + " passed, " + str(failed_count) + " failed")


if __name__ == "__main__":
    run_tests()
