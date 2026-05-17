from same_tree import TreeNode, is_same_tree


def test_same_tree():
    print("Testing is_same_tree...")

    # Test case 1: p=[1,2,3], q=[1,2,3] -> True
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    result = is_same_tree(p, q)
    expected = True
    print(f"is_same_tree([1,2,3], [1,2,3]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: p=[1,2], q=[1,null,2] -> False
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = None
    q = TreeNode(1)
    q.left = None
    q.right = TreeNode(2)
    result = is_same_tree(p, q)
    expected = False
    print(f"is_same_tree([1,2], [1,null,2]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: p=[1,2,1], q=[1,1,2] -> False
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    result = is_same_tree(p, q)
    expected = False
    print(f"is_same_tree([1,2,1], [1,1,2]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: Both empty -> True
    result = is_same_tree(None, None)
    expected = True
    print(f"is_same_tree([], []) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: p=[1], q=[] -> False
    p = TreeNode(1)
    result = is_same_tree(p, None)
    expected = False
    print(f"is_same_tree([1], []) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_same_tree()
