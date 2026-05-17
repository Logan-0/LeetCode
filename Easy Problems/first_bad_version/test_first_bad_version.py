from first_bad_version import first_bad_version, is_bad_version, first_bad


def test_first_bad_version():
    print("Testing first_bad_version...")

    # Test case 1: n=5, bad=4 -> 4
    global first_bad
    first_bad = 4
    result = first_bad_version(5)
    expected = 4
    print(f"first_bad_version(5) with bad=4 = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: n=1, bad=1 -> 1
    first_bad = 1
    result = first_bad_version(1)
    expected = 1
    print(f"first_bad_version(1) with bad=1 = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: n=10, bad=1 -> 1
    first_bad = 1
    result = first_bad_version(10)
    expected = 1
    print(f"first_bad_version(10) with bad=1 = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: n=10, bad=10 -> 10
    first_bad = 10
    result = first_bad_version(10)
    expected = 10
    print(f"first_bad_version(10) with bad=10 = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: n=5, bad=2 -> 2
    first_bad = 2
    result = first_bad_version(5)
    expected = 2
    print(f"first_bad_version(5) with bad=2 = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_first_bad_version()
