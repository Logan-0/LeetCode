from plus_one import plus_one


def test_plus_one():
    print("Testing plus_one...")

    # Test case 1: [1,2,3] -> [1,2,4]
    result = plus_one([1, 2, 3])
    expected = [1, 2, 4]
    print(f"plus_one([1,2,3]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: [4,3,2,1] -> [4,3,2,2]
    result = plus_one([4, 3, 2, 1])
    expected = [4, 3, 2, 2]
    print(f"plus_one([4,3,2,1]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: [9] -> [1,0]
    result = plus_one([9])
    expected = [1, 0]
    print(f"plus_one([9]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: [9,9] -> [1,0,0]
    result = plus_one([9, 9])
    expected = [1, 0, 0]
    print(f"plus_one([9,9]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: [1,9,9] -> [2,0,0]
    result = plus_one([1, 9, 9])
    expected = [2, 0, 0]
    print(f"plus_one([1,9,9]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 6: [0] -> [1]
    result = plus_one([0])
    expected = [1]
    print(f"plus_one([0]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_plus_one()
