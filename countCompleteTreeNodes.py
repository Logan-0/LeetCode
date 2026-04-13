class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_level_order(values: list[int | None]) -> TreeNode | None:
    if not values:
        return None
    if values[0] is None:
        return None

    nodes: list[TreeNode | None] = [None] * len(values)
    nodes[0] = TreeNode(values[0])

    for i in range(len(values)):
        if values[i] is None:
            continue
        if nodes[i] is None:
            nodes[i] = TreeNode(values[i])

        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(values) and values[left_i] is not None:
            nodes[left_i] = TreeNode(values[left_i])
            nodes[i].left = nodes[left_i]
        if right_i < len(values) and values[right_i] is not None:
            nodes[right_i] = TreeNode(values[right_i])
            nodes[i].right = nodes[right_i]

    return nodes[0]


class Solution:

    def countCompleteTreeNodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1 + self.countCompleteTreeNodes(root.left) + self.countCompleteTreeNodes(root.right)



def main() -> None:
    root = build_tree_level_order([1, 4, 6, 3, 66, 23, 54, 11, 90, 84])
    solution = Solution().countCompleteTreeNodes(root)
    print(solution)

if __name__ == "__main__":
    main()