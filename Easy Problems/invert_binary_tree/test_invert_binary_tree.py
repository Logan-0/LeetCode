from invert_binary_tree import TreeNode, invert_tree


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Helper function to convert tree to list for comparison"""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


def test_invert_binary_tree():
    print("Testing invert_tree...")

    # Test case 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    inverted = invert_tree(root)
    result = tree_to_list(inverted)
    expected = [4, 7, 2, 9, 6, 3, 1]
    print(f"invert_tree([4,2,7,1,3,6,9]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: [2,1,3] -> [2,3,1]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    inverted = invert_tree(root)
    result = tree_to_list(inverted)
    expected = [2, 3, 1]
    print(f"invert_tree([2,1,3]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: [] -> []
    result = invert_tree(None)
    expected = None
    print(f"invert_tree([]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_invert_binary_tree()
