class TreeNode:
    """
    Represents a node in a binary tree.
    Each node stores a value and references to its left and right children.
    """
    def __init__(self, value: int = 0, left_child=None, right_child=None):
        """
        Initialize a new tree node.

        Args:
            value: The integer value stored in this node
            left_child: Reference to the left child node (None if absent)
            right_child: Reference to the right child node (None if absent)
        """
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def build_tree_level_order(values: list) -> TreeNode | None:
    """
    Helper function: builds a binary tree from a level-order list.
    None entries in the list represent missing nodes.

    Args:
        values: Level-order list of values (None = missing node)

    Returns:
        The root of the constructed tree, or None if the list is empty
    """
    if not values or values[0] is None:
        return None

    all_nodes: list[TreeNode | None] = [None] * len(values)
    all_nodes[0] = TreeNode(values[0])

    for current_index in range(len(values)):
        if values[current_index] is None:
            continue
        if all_nodes[current_index] is None:
            all_nodes[current_index] = TreeNode(values[current_index])

        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if left_index < len(values) and values[left_index] is not None:
            all_nodes[left_index] = TreeNode(values[left_index])
            all_nodes[current_index].left_child = all_nodes[left_index]

        if right_index < len(values) and values[right_index] is not None:
            all_nodes[right_index] = TreeNode(values[right_index])
            all_nodes[current_index].right_child = all_nodes[right_index]

    return all_nodes[0]


def max_depth(root_node: TreeNode | None) -> int:
    """
    Given the root of a binary tree, return its maximum depth.
    The maximum depth is the number of nodes along the longest path from the
    root down to the farthest leaf node.

    LeetCode #104 - Maximum Depth of Binary Tree
    Difficulty: Easy
    Pattern: Tree / DFS (Recursion)

    Example:
        Input:  [3, 9, 20, None, None, 15, 7]   (level-order)
                      3
                     / \\
                    9  20
                       / \\
                      15   7
        Output: 3

        Input:  []
        Output: 0

    Hint: The depth of a tree is 1 + the maximum of the depths of its two
          subtrees. The depth of an empty tree (None) is 0.

    Time complexity goal: O(n)
    Space complexity goal: O(h) where h is the height of the tree

    Args:
        root_node: The root of the binary tree (None for an empty tree)

    Returns:
        The maximum depth of the tree
    """
    if root_node is None:
        return 0

    left_depth = max_depth(root_node.left_child)
    right_depth = max_depth(root_node.right_child)

    return 1 + max(left_depth, right_depth)


def main() -> None:
    """
    Main function to demonstrate the max_depth function.
    """
    root = build_tree_level_order([3, 9, 20, None, None, 15, 7])
    result = max_depth(root)
    print("Maximum depth: " + str(result))


if __name__ == "__main__":
    main()
