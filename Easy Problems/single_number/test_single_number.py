from single_number import single_number


def test_single_number():
    print("Testing single_number...")

    # Test case 1: [2,2,1] -> 1
    result = single_number([2, 2, 1])
    expected = 1
    print(f"single_number([2,2,1]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: [4,1,2,1,2] -> 4
    result = single_number([4, 1, 2, 1, 2])
    expected = 4
    print(f"single_number([4,1,2,1,2]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: [1] -> 1
    result = single_number([1])
    expected = 1
    print(f"single_number([1]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: [2,2,3,3,4] -> 4
    result = single_number([2, 2, 3, 3, 4])
    expected = 4
    print(f"single_number([2,2,3,3,4]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: [1,1,2,2,3,3,4,4,5] -> 5
    result = single_number([1, 1, 2, 2, 3, 3, 4, 4, 5])
    expected = 5
    print(f"single_number([1,1,2,2,3,3,4,4,5]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_single_number()
