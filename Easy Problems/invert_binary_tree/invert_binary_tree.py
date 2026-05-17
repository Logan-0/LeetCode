class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """
    Given the root of a binary tree, invert the tree, and return its root.

    LeetCode #226 - Invert Binary Tree
    Difficulty: Easy
    Pattern: Tree / DFS

    Example:
        Input:  root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]

    Hint: Swap the left and right children of each node recursively.
          The inversion happens in place.

    Time complexity goal: O(n)
    Space complexity goal: O(h) - recursion stack height

    Args:
        root: The root of a binary tree

    Returns:
        The root of the inverted tree
    """
    pass


def main() -> None:
    """
    Main function to demonstrate invert_tree with examples.
    """
    # Example: [4,2,7,1,3,6,9]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    inverted = invert_tree(root)
    print("Tree inverted successfully")


if __name__ == "__main__":
    main()
