class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Given the roots of two binary trees p and q, write a function to check if they
    are the same or not.

    Two binary trees are considered the same if they are structurally identical,
    and the nodes have the same value.

    LeetCode #100 - Same Tree
    Difficulty: Easy
    Pattern: Tree / DFS

    Example:
        Input:  p = [1,2,3], q = [1,2,3]
        Output: True

        Input:  p = [1,2], q = [1,null,2]
        Output: False

    Hint: Use recursion. Compare the current nodes, then recursively compare
          left subtrees and right subtrees.

    Time complexity goal: O(min(m,n)) - where m and n are the number of nodes
    Space complexity goal: O(h) - recursion stack height

    Args:
        p: Root of the first binary tree
        q: Root of the second binary tree

    Returns:
        True if the trees are the same, False otherwise
    """
    pass


def main() -> None:
    """
    Main function to demonstrate is_same_tree with examples.
    """
    # Example: p = [1,2,3], q = [1,2,3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    result = is_same_tree(p, q)
    print("Are trees the same: " + str(result))


if __name__ == "__main__":
    main()
