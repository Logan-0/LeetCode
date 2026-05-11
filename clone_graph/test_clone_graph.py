from clone_graph import Node, clone_graph


def test_clone_graph():
    print("Testing clone_graph...")

    # Test case 1: [[2,4],[1,3],[2,4],[1,3]]
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned = clone_graph(node1)
    # Check that clone is not the same object
    assert cloned is not node1, "FAIL: Clone should be a different object"
    # Check that clone has correct value
    assert cloned.val == 1, f"FAIL: Expected val 1, got {cloned.val}"
    # Check that clone has correct number of neighbors
    assert len(cloned.neighbors) == 2, f"FAIL: Expected 2 neighbors, got {len(cloned.neighbors)}"
    print(f"clone_graph([[2,4],[1,3],[2,4],[1,3]]) = cloned successfully")

    # Test case 2: [[]] (single node with no neighbors)
    node = Node(1)
    cloned = clone_graph(node)
    assert cloned is not node, "FAIL: Clone should be a different object"
    assert cloned.val == 1, f"FAIL: Expected val 1, got {cloned.val}"
    assert len(cloned.neighbors) == 0, f"FAIL: Expected 0 neighbors, got {len(cloned.neighbors)}"
    print(f"clone_graph([[]]) = cloned successfully")

    # Test case 3: None
    cloned = clone_graph(None)
    assert cloned is None, "FAIL: Expected None, got a node"
    print(f"clone_graph(None) = None")

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_clone_graph()
