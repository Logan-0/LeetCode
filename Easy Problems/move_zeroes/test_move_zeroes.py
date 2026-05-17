from move_zeroes import move_zeroes


def test_move_zeroes():
    print("Testing move_zeroes...")

    # Test case 1: [0,1,0,3,12] -> [1,3,12,0,0]
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    expected = [1, 3, 12, 0, 0]
    print(f"move_zeroes([0,1,0,3,12]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 2: [0] -> [0]
    nums = [0]
    move_zeroes(nums)
    expected = [0]
    print(f"move_zeroes([0]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 3: [1,0,2,0,3] -> [1,2,3,0,0]
    nums = [1, 0, 2, 0, 3]
    move_zeroes(nums)
    expected = [1, 2, 3, 0, 0]
    print(f"move_zeroes([1,0,2,0,3]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 4: [1,2,3] -> [1,2,3] (no zeros)
    nums = [1, 2, 3]
    move_zeroes(nums)
    expected = [1, 2, 3]
    print(f"move_zeroes([1,2,3]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    # Test case 5: [0,0,0,1] -> [1,0,0,0]
    nums = [0, 0, 0, 1]
    move_zeroes(nums)
    expected = [1, 0, 0, 0]
    print(f"move_zeroes([0,0,0,1]) = {nums}, expected {expected}")
    assert nums == expected, f"FAIL: Expected {expected}, got {nums}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_move_zeroes()
