import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from group_anagrams import group_anagrams


def normalize(groups: list[list[str]]) -> list[list[str]]:
    """
    Sort each group internally and then sort the list of groups so that
    comparisons are order-independent.
    """
    return sorted([sorted(group) for group in groups])


def run_tests() -> None:
    test_cases = [
        {
            "description": "classic example -- three anagram groups",
            "input": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        },
        {
            "description": "single empty string",
            "input": [""],
            "expected": [[""]],
        },
        {
            "description": "single word",
            "input": ["a"],
            "expected": [["a"]],
        },
        {
            "description": "all words are anagrams of each other",
            "input": ["abc", "bca", "cab"],
            "expected": [["abc", "bca", "cab"]],
        },
        {
            "description": "no anagram pairs -- each word in its own group",
            "input": ["cat", "dog", "bird"],
            "expected": [["bird"], ["cat"], ["dog"]],
        },
        {
            "description": "two groups",
            "input": ["ab", "ba", "cd", "dc"],
            "expected": [["ab", "ba"], ["cd", "dc"]],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = group_anagrams(test["input"])
        if normalize(result) == normalize(test["expected"]):
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  input:    " + str(test["input"]))
            print("  expected: " + str(normalize(test["expected"])))
            print("  got:      " + str(normalize(result)))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
