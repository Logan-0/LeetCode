from symmetric_tree import TreeNode, is_symmetric


def test_symmetric_tree():
    print("Testing is_symmetric...")

    # Test case 1: [1,2,2,3,4,4,3] -> True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    result = is_symmetric(root)
    expected = True
    print(f"is_symmetric([1,2,2,3,4,4,3]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: [1,2,2,null,3,null,3] -> False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = None
    root.left.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(3)
    result = is_symmetric(root)
    expected = False
    print(f"is_symmetric([1,2,2,null,3,null,3]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: [1] -> True
    root = TreeNode(1)
    result = is_symmetric(root)
    expected = True
    print(f"is_symmetric([1]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: [] -> True
    result = is_symmetric(None)
    expected = True
    print(f"is_symmetric([]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: [1,2,2] -> True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    result = is_symmetric(root)
    expected = True
    print(f"is_symmetric([1,2,2]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_symmetric_tree()
