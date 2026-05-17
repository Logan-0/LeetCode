from permutations import permute


def test_permutations():
    print("Testing permute...")

    # Test case 1: [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    result = permute([1, 2, 3])
    # Sort each permutation and the result for comparison
    result_sorted = [sorted(p) for p in result]
    # Check we have 6 permutations
    assert len(result) == 6, f"FAIL: Expected 6 permutations, got {len(result)}"
    # Check all permutations are unique
    unique_perms = set(tuple(p) for p in result)
    assert len(unique_perms) == 6, f"FAIL: Expected 6 unique permutations, got {len(unique_perms)}"
    print(f"permute([1,2,3]) has {len(result)} permutations")

    # Test case 2: [0,1] -> [[0,1],[1,0]]
    result = permute([0, 1])
    assert len(result) == 2, f"FAIL: Expected 2 permutations, got {len(result)}"
    unique_perms = set(tuple(p) for p in result)
    assert len(unique_perms) == 2, f"FAIL: Expected 2 unique permutations, got {len(unique_perms)}"
    print(f"permute([0,1]) has {len(result)} permutations")

    # Test case 3: [1] -> [[1]]
    result = permute([1])
    assert len(result) == 1, f"FAIL: Expected 1 permutation, got {len(result)}"
    assert result == [[1]], f"FAIL: Expected [[1]], got {result}"
    print(f"permute([1]) = {result}")

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_permutations()
