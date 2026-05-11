from subsets import subsets


def test_subsets():
    print("Testing subsets...")

    # Test case 1: [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    result = subsets([1, 2, 3])
    # Sort each subset and the result for comparison
    result_sorted = [sorted(subset) for subset in result]
    result_sorted.sort()
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    expected_sorted = [sorted(subset) for subset in expected]
    expected_sorted.sort()
    print(f"subsets([1,2,3]) has {len(result)} subsets, expected {len(expected)}")
    assert result_sorted == expected_sorted, f"FAIL: Expected {expected_sorted}, got {result_sorted}"

    # Test case 2: [0] -> [[],[0]]
    result = subsets([0])
    result_sorted = [sorted(subset) for subset in result]
    result_sorted.sort()
    expected = [[], [0]]
    expected_sorted = [sorted(subset) for subset in expected]
    expected_sorted.sort()
    print(f"subsets([0]) = {result_sorted}, expected {expected_sorted}")
    assert result_sorted == expected_sorted, f"FAIL: Expected {expected_sorted}, got {result_sorted}"

    # Test case 3: [1] -> [[],[1]]
    result = subsets([1])
    result_sorted = [sorted(subset) for subset in result]
    result_sorted.sort()
    expected = [[], [1]]
    expected_sorted = [sorted(subset) for subset in expected]
    expected_sorted.sort()
    print(f"subsets([1]) = {result_sorted}, expected {expected_sorted}")
    assert result_sorted == expected_sorted, f"FAIL: Expected {expected_sorted}, got {result_sorted}"

    # Test case 4: [] -> [[]]
    result = subsets([])
    result_sorted = [sorted(subset) for subset in result]
    result_sorted.sort()
    expected = [[]]
    expected_sorted = [sorted(subset) for subset in expected]
    expected_sorted.sort()
    print(f"subsets([]) = {result_sorted}, expected {expected_sorted}")
    assert result_sorted == expected_sorted, f"FAIL: Expected {expected_sorted}, got {result_sorted}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_subsets()
