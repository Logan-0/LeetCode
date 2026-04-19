import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from minStack import create_min_stack


def run_tests() -> None:
    passed = 0
    failed = 0

    def check(description: str, result, expected) -> None:
        nonlocal passed, failed
        if result == expected:
            print("PASS: " + description)
            passed += 1
        else:
            print("FAIL: " + description)
            print("  expected: " + str(expected))
            print("  got:      " + str(result))
            failed += 1

    # Test 1: basic push/top/get_min sequence
    stack = create_min_stack()
    stack["push"](5)
    stack["push"](3)
    stack["push"](8)
    check("push 5,3,8 -- top is 8", stack["top"](), 8)
    check("push 5,3,8 -- min is 3", stack["get_min"](), 3)

    # Test 2: new minimum pushed
    stack["push"](1)
    check("push 1 -- min updates to 1", stack["get_min"](), 1)
    check("push 1 -- top is 1", stack["top"](), 1)

    # Test 3: pop removes the minimum, restores old minimum
    stack["pop"]()
    check("pop 1 -- min restores to 3", stack["get_min"](), 3)
    check("pop 1 -- top is now 8", stack["top"](), 8)

    # Test 4: min stays correct when popping non-minimum elements
    stack["pop"]()
    check("pop 8 -- min still 3", stack["get_min"](), 3)
    stack["pop"]()
    check("pop 3 -- min is now 5", stack["get_min"](), 5)

    # Test 5: fresh stack with duplicate minimums
    stack2 = create_min_stack()
    stack2["push"](2)
    stack2["push"](2)
    stack2["push"](2)
    check("three equal pushes -- min is 2", stack2["get_min"](), 2)
    stack2["pop"]()
    check("pop one 2 -- min still 2 (duplicates)", stack2["get_min"](), 2)

    # Test 6: negative numbers
    stack3 = create_min_stack()
    stack3["push"](10)
    stack3["push"](-5)
    stack3["push"](3)
    check("negative number is the min", stack3["get_min"](), -5)
    stack3["pop"]()
    check("pop 3 -- min still -5", stack3["get_min"](), -5)
    stack3["pop"]()
    check("pop -5 -- min restores to 10", stack3["get_min"](), 10)

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
