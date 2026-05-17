import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from kthLargestElement import create_kth_largest


def run_tests() -> None:
    passed = 0
    failed = 0

    def check(description: str, result: int, expected: int) -> None:
        nonlocal passed, failed
        if result == expected:
            print("PASS: " + description)
            passed += 1
        else:
            print("FAIL: " + description)
            print("  expected: " + str(expected))
            print("  got:      " + str(result))
            failed += 1

    # Test 1: k=3, build from [4,5,8,2]. The 3 largest are [4,5,8], min is 4.
    add_number = create_kth_largest(3, [4, 5, 8, 2])
    check("k=3, init=[4,5,8,2], add 3 -- below k-th, stays 4", add_number(3), 4)
    check("k=3, add 5 -- ties k-th, 5 becomes new k-th", add_number(5), 5)
    check("k=3, add 10 -- larger than all, k-th is now 5", add_number(10), 5)
    check("k=3, add 9 -- [8,9,10] in heap, k-th is 8", add_number(9), 8)
    check("k=3, add 4 -- below k-th, stays 8", add_number(4), 8)

    # Test 2: k=1 always returns the maximum
    add_max = create_kth_largest(1, [3, 1, 2])
    check("k=1, init=[3,1,2], add 4 -- max is now 4", add_max(4), 4)
    check("k=1, add 0 -- max stays 4", add_max(0), 4)
    check("k=1, add 10 -- max is now 10", add_max(10), 10)

    # Test 3: k=2, empty initial list, stream builds up
    add_second = create_kth_largest(2, [])
    add_second(1)
    result = add_second(2)
    check("k=2, init=[], after adding 1 and 2 -- 2nd largest is 1", result, 1)
    result = add_second(3)
    check("k=2, add 3 -- 2nd largest is now 2", result, 2)

    print("\nResults: " + str(passed) + " passed, " + str(failed) + " failed")


if __name__ == "__main__":
    run_tests()
