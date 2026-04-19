import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from verifyingAlienDictionary import verify_dictionary


# Standard English order used for some tests
ENGLISH_ORDER = "abcdefghijklmnopqrstuvwxyz"


def run_tests() -> None:
    test_cases = [
        {
            "description": "correctly sorted in standard English order",
            "words": ["apple", "banana", "cherry"],
            "order": ENGLISH_ORDER,
            "expected": True,
        },
        {
            "description": "NOT sorted in standard English order",
            "words": ["banana", "apple"],
            "order": ENGLISH_ORDER,
            "expected": False,
        },
        {
            "description": "alien order where h comes first -- words sorted correctly",
            "words": ["hello", "leetcode"],
            "order": "hlabcdefgijkmnopqrstuvwxyz",
            "expected": True,
        },
        {
            "description": "single word -- always sorted",
            "words": ["word"],
            "order": ENGLISH_ORDER,
            "expected": True,
        },
        {
            "description": "prefix word before extended word -- correct order",
            "words": ["app", "apple"],
            "order": ENGLISH_ORDER,
            "expected": True,
        },
        {
            "description": "extended word before prefix word -- incorrect order",
            "words": ["apple", "app"],
            "order": ENGLISH_ORDER,
            "expected": False,
        },
        {
            "description": "all same words -- considered sorted",
            "words": ["word", "word"],
            "order": ENGLISH_ORDER,
            "expected": True,
        },
        {
            "description": "alien order reverses a and b -- 'b' should precede 'a' words",
            "words": ["bat", "ant"],
            "order": "bcadefghijklmnopqrstuvwxyz",
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = verify_dictionary(test["words"], test["order"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  words:    " + str(test["words"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
