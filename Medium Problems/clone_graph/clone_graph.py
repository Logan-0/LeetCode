class Node:
    """
    Definition for a Node in a graph.
    """
    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    """
    Given a reference of a node in a connected undirected graph, return a deep copy
    (clone) of the graph. Each node in the graph contains a val (int) and a list
    (List[Node]) of its neighbors.

    LeetCode #133 - Clone Graph
    Difficulty: Medium
    Pattern: Graph / BFS / DFS

    Example:
        Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]

    Hint: Use BFS or DFS to traverse the graph while keeping a hash map of
          original nodes to their clones to avoid cycles.

    Time complexity goal: O(V + E) - V = vertices, E = edges
    Space complexity goal: O(V)

    Args:
        node: A reference to a node in the graph

    Returns:
        A deep copy of the graph
    """
    pass


def main() -> None:
    """
    Main function to demonstrate clone_graph with examples.
    """
    # Example: [[2,4],[1,3],[2,4],[1,3]]
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned = clone_graph(node1)
    print("Graph cloned successfully")


if __name__ == "__main__":
    main()
