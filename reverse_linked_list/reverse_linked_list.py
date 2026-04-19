class ListNode:
    """
    Represents a single node in a singly linked list.
    Each node holds a value and a reference to the next node in the chain.
    """

    def __init__(self, value: int = 0, next_node=None):
        """
        Args:
            value: The integer stored in this node
            next_node: The next ListNode in the list, or None if this is the tail
        """
        self.value = value
        self.next_node = next_node


def list_to_nodes(values: list[int]) -> ListNode | None:
    """
    Helper: converts a Python list into a linked list and returns the head node.

    Args:
        values: A list of integers to convert

    Returns:
        The head of the resulting linked list, or None if values is empty
    """
    dummy_head = ListNode(0)
    current_node = dummy_head

    for current_value in values:
        current_node.next_node = ListNode(current_value)
        current_node = current_node.next_node

    return dummy_head.next_node


def nodes_to_list(head_node: ListNode | None) -> list[int]:
    """
    Helper: converts a linked list back into a Python list for easy inspection.

    Args:
        head_node: The head of the linked list

    Returns:
        A Python list containing all values from the linked list in order
    """
    result = []
    current_node = head_node

    while current_node is not None:
        result.append(current_node.value)
        current_node = current_node.next_node

    return result


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    """
    Reverses a singly linked list in place and returns the new head.

    The iterative approach uses three variables:
    - previous_node: the node that the current node's arrow should point to
    - current_node: the node whose arrow we are currently flipping
    - next_node: a saved reference to the original next node before we overwrite it

    We walk through the list once, flipping each "next" pointer to point backward
    instead of forward. At the end, previous_node is sitting on the old tail,
    which is now the new head.

    Visual for [1 -> 2 -> 3 -> None]:
    Step 1: previous=None, current=1  --> flip: 1->None,  advance to current=2
    Step 2: previous=1,    current=2  --> flip: 2->1,     advance to current=3
    Step 3: previous=2,    current=3  --> flip: 3->2,     advance to current=None
    Loop ends. previous=3, which is the new head of [3 -> 2 -> 1 -> None].

    Args:
        head: The head of the linked list to reverse

    Returns:
        The new head of the reversed list (the old tail node)

    Time Complexity: O(n) -- single pass through the list
    Space Complexity: O(1) -- only three pointer variables used
    """

    previous_node = None
    current_node = head

    while current_node is not None:
        # Save the next node before we overwrite the pointer
        next_node = current_node.next_node

        # Flip the arrow to point backward
        current_node.next_node = previous_node

        # Advance both pointers one step forward
        previous_node = current_node
        current_node = next_node

    # current_node is None; previous_node is the last node we visited (new head)
    return previous_node


def main() -> None:
    """
    Main function to demonstrate reverse_linked_list with examples.
    """
    original_values = [1, 2, 3, 4, 5]
    head = list_to_nodes(original_values)

    print("Original list: " + str(nodes_to_list(head)))

    reversed_head = reverse_linked_list(head)

    print("Reversed list: " + str(nodes_to_list(reversed_head)))


if __name__ == "__main__":
    main()
