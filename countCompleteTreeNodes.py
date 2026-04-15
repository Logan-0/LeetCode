class TreeNode:
    """
    This class represents a node in a binary tree.
    A binary tree is like a family tree where each person (node) can have up to two children.
    Each node stores a value and references to its left and right children.
    """
    def __init__(self, value: int = 0, left_child=None, right_child=None):
        """
        Initialize a new tree node with a value and references to children.
        
        Args:
            value: The integer value stored in this node
            left_child: Reference to the left child node (or None if no left child)
            right_child: Reference to the right child node (or None if no right child)
        """
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def build_tree_level_order(values: list[int | None]) -> TreeNode | None:
    """
    This helper function builds a binary tree from a list using level-order traversal.
    Level-order means we fill the tree level by level, left to right.
    None values represent missing nodes.
    
    For example, [1, 4, 6, 3, 66] creates:
            1
           / \
          4   6
         / \
        3  66
    
    Args:
        values: A list of values where None represents a missing node
        
    Returns:
        The root (top node) of the tree, or None if the list is empty
    """
    # If the list is empty, there's no tree to build
    if not values:

        return None
    
    # If the first value is None, there's no root node
    if values[0] is None:

        return None

    # Create an array to store all nodes (some will be None)
    all_nodes: list[TreeNode | None] = [None] * len(values)
    
    # Create the root node (first element in the list)
    all_nodes[0] = TreeNode(values[0])

    # Build the tree level by level
    for current_index in range(len(values)):

        current_value = values[current_index]
        
        # Skip None values (they represent missing nodes)
        if current_value is None:
            continue
        
        # If this position doesn't have a node yet, create one
        if all_nodes[current_index] is None:
            all_nodes[current_index] = TreeNode(current_value)

        # Calculate the indices for left and right children
        # In a level-order array, left child is at 2*i + 1, right child is at 2*i + 2
        left_child_index = 2 * current_index + 1
        right_child_index = 2 * current_index + 2

        # Create and link the left child if it exists
        if left_child_index < len(values) and values[left_child_index] is not None:

            all_nodes[left_child_index] = TreeNode(values[left_child_index])
            all_nodes[current_index].left_child = all_nodes[left_child_index]
        
        # Create and link the right child if it exists
        if right_child_index < len(values) and values[right_child_index] is not None:
            
            all_nodes[right_child_index] = TreeNode(values[right_child_index])
            all_nodes[current_index].right_child = all_nodes[right_child_index]

    # Return the root node (first node in the array)
    return all_nodes[0]


def count_complete_tree_nodes(root_node: TreeNode | None) -> int:
    """
    This function counts the total number of nodes in a binary tree.
    It uses recursion - a technique where a function calls itself.
    
    The approach:
    1. If the current node is None, count is 0
    2. Otherwise, count = 1 (for current node) + count of left subtree + count of right subtree
    
    Think of it like counting people in a family tree:
    - Count yourself (1)
    - Add the count of everyone in your left branch
    - Add the count of everyone in your right branch
    
    Args:
        root_node: The root (top node) of the tree
        
    Returns:
        The total number of nodes in the tree
    """
    
    # Base case: if this node doesn't exist, count is 0
    if root_node is None:
        return 0
    
    # Recursive case: count this node (1) plus all nodes in left and right subtrees
    nodes_in_left_subtree = count_complete_tree_nodes(root_node.left_child)
    nodes_in_right_subtree = count_complete_tree_nodes(root_node.right_child)
    
    return 1 + nodes_in_left_subtree + nodes_in_right_subtree


def main() -> None:
    """
    Main function to demonstrate the count_complete_tree_nodes function with an example.
    """
    # Example: Build a tree with values [1, 4, 6, 3, 66, 23, 54, 11, 90, 84]
    # This creates a tree with 10 nodes
    tree_root = build_tree_level_order([1, 4, 6, 3, 66, 23, 54, 11, 90, 84])
    
    total_nodes = count_complete_tree_nodes(tree_root)
    print("Total number of nodes in the tree: " + str(total_nodes))

if __name__ == "__main__":
    main()