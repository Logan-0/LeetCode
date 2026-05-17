from sort_colors import sort_colors


def test_sort_colors():
    print("Testing sort_colors...")

    # Test case 1: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    expected = [0, 0, 1, 1, 2, 2]
    print(f"sort_colors([2,0,2,1,1,0]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 2: [2,0,1] -> [0,1,2]
    nums = [2, 0, 1]
    sort_colors(nums)
    expected = [0, 1, 2]
    print(f"sort_colors([2,0,1]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 3: [0] -> [0]
    nums = [0]
    sort_colors(nums)
    expected = [0]
    print(f"sort_colors([0]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 4: [1] -> [1]
    nums = [1]
    sort_colors(nums)
    expected = [1]
    print(f"sort_colors([1]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 5: [2,2,2,0,0,0,1,1,1] -> [0,0,0,1,1,1,2,2,2]
    nums = [2, 2, 2, 0, 0, 0, 1, 1, 1]
    sort_colors(nums)
    expected = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    print(f"sort_colors([2,2,2,0,0,0,1,1,1]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 6: [1,0,2] -> [0,1,2]
    nums = [1, 0, 2]
    sort_colors(nums)
    expected = [0, 1, 2]
    print(f"sort_colors([1,0,2]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_sort_colors()
