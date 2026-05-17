from search_insert_position import search_insert


def test_search_insert_position():
    print("Testing search_insert...")

    # Test case 1: [1,3,5,6], target=5 -> 2
    result = search_insert([1, 3, 5, 6], 5)
    expected = 2
    print(f"search_insert([1,3,5,6], 5) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: [1,3,5,6], target=2 -> 1
    result = search_insert([1, 3, 5, 6], 2)
    expected = 1
    print(f"search_insert([1,3,5,6], 2) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: [1,3,5,6], target=7 -> 4
    result = search_insert([1, 3, 5, 6], 7)
    expected = 4
    print(f"search_insert([1,3,5,6], 7) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: [1,3,5,6], target=0 -> 0
    result = search_insert([1, 3, 5, 6], 0)
    expected = 0
    print(f"search_insert([1,3,5,6], 0) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: [1], target=0 -> 0
    result = search_insert([1], 0)
    expected = 0
    print(f"search_insert([1], 0) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 6: [1], target=1 -> 0
    result = search_insert([1], 1)
    expected = 0
    print(f"search_insert([1], 1) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 7: [1], target=2 -> 1
    result = search_insert([1], 2)
    expected = 1
    print(f"search_insert([1], 2) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_search_insert_position()
