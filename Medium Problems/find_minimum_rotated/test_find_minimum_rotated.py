from find_minimum_rotated import find_min


def test_find_min():
    print("Testing find_min...")

    # Test case 1: [3,4,5,1,2] -> 1
    result = find_min([3, 4, 5, 1, 2])
    expected = 1
    print(f"find_min([3,4,5,1,2]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: [4,5,6,7,0,1,2] -> 0
    result = find_min([4, 5, 6, 7, 0, 1, 2])
    expected = 0
    print(f"find_min([4,5,6,7,0,1,2]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: [11,13,15,17] -> 11
    result = find_min([11, 13, 15, 17])
    expected = 11
    print(f"find_min([11,13,15,17]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: [1] -> 1
    result = find_min([1])
    expected = 1
    print(f"find_min([1]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: [2,1] -> 1
    result = find_min([2, 1])
    expected = 1
    print(f"find_min([2,1]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 6: [3,1,2] -> 1
    result = find_min([3, 1, 2])
    expected = 1
    print(f"find_min([3,1,2]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_find_min()
