import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from closestTargerCircleArray import find_closest_target_distance


def run_tests() -> None:
    test_cases = [
        {
            "description": "target appears twice -- backward wrap is shorter (distance 1)",
            "words": ["cat", "dog", "fish", "bird", "fish"],
            "target": "fish",
            "start": 0,
            "expected": 1,
        },
        {
            "description": "target appears once in the middle",
            "words": ["cat", "dog", "fish", "bird"],
            "target": "fish",
            "start": 0,
            "expected": 2,
        },
        {
            "description": "starting position IS the target -- distance 0",
            "words": ["cat", "dog", "fish", "bird"],
            "target": "fish",
            "start": 2,
            "expected": 0,
        },
        {
            "description": "target is the first element -- distance 1 backward from last",
            "words": ["cat", "dog", "fish", "bird"],
            "target": "cat",
            "start": 3,
            "expected": 1,
        },
        {
            "description": "target not in array -- returns -1",
            "words": ["cat", "dog", "bird"],
            "target": "fish",
            "start": 0,
            "expected": -1,
        },
        {
            "description": "single element array -- target is at start",
            "words": ["fish"],
            "target": "fish",
            "start": 0,
            "expected": 0,
        },
        {
            "description": "equidistant forward and backward",
            "words": ["a", "b", "c", "d", "e"],
            "target": "c",
            "start": 0,
            "expected": 2,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        result = find_closest_target_distance(test["words"], test["target"], test["start"])
        if result == test["expected"]:
            print("PASS: " + test["description"])
            passed += 1
        else:
            print("FAIL: " + test["description"])
            print("  words:    " + str(test["words"]))
            print("  target:   " + str(test["target"]))
            print("  start:    " + str(test["start"]))
            print("  expected: " + str(test["expected"]))
            print("  got:      " + str(result))
            failed += 1

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
