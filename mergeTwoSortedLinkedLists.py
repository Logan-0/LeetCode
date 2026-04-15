class ListNode:
    """
    This class represents a node in a linked list.
    A linked list is like a chain where each link points to the next one.
    Each node stores a value and a reference (pointer) to the next node.
    """
    def __init__(self, value: int = 0, next_node=None):
        """
        Initialize a new node with a value and a reference to the next node.
        
        Args:
            value: The integer value stored in this node
            next_node: Reference to the next node in the list (None if this is the last node)
        """
        self.value = value
        self.next_node = next_node


def list_to_nodes(values: list[int]) -> ListNode | None:
    """
    This helper function converts a regular Python list into a linked list.
    Each element in the list becomes a node in the linked list.
    
    Args:
        values: A list of integers to convert to a linked list
        
    Returns:
        The head (first node) of the linked list, or None if the list is empty
    """
    # Create a dummy node to simplify the building process
    # We'll skip this dummy node in the final result
    dummy_head = ListNode(0)
    current_node = dummy_head
    
    # Create a node for each value and link them together
    for current_value in values:
        current_node.next_node = ListNode(current_value)
        current_node = current_node.next_node
    
    # Return the first actual node (skip the dummy)
    return dummy_head.next_node


def nodes_to_list(head_node: ListNode | None) -> list[int]:
    """
    This helper function converts a linked list back into a regular Python list.
    We traverse the linked list from the head to the end, collecting all values.
    
    Args:
        head_node: The head (first node) of the linked list
        
    Returns:
        A Python list containing all values from the linked list
    """
    result_list: list[int] = []
    current_node = head_node
    
    # Traverse the linked list until we reach the end (None)
    while current_node is not None:
        result_list.append(current_node.value)
        current_node = current_node.next_node
    
    return result_list


def merge_two_lists(first_list_head: ListNode | None, second_list_head: ListNode | None) -> ListNode | None:
    """
    This function merges two sorted linked lists into one sorted linked list.
    Both input lists must already be sorted in ascending order.
    
    The approach is similar to merging two sorted decks of cards:
    - Look at the top card of each deck
    - Pick the smaller one and add it to your merged deck
    - Repeat until one deck is empty
    - Add all remaining cards from the other deck
    
    Args:
        first_list_head: The head of the first sorted linked list
        second_list_head: The head of the second sorted linked list
        
    Returns:
        The head of the merged sorted linked list
    """
    
    # Create a dummy head to simplify building the result list
    dummy_result_head = ListNode(0)
    current_result_tail = dummy_result_head

    # Process both lists while both still have nodes
    while first_list_head is not None and second_list_head is not None:
        
        # Compare the current nodes from both lists
        if first_list_head.value < second_list_head.value:
            # First list's node is smaller, add it to result
            current_result_tail.next_node = first_list_head
            first_list_head = first_list_head.next_node
        else:
            # Second list's node is smaller or equal, add it to result
            current_result_tail.next_node = second_list_head
            second_list_head = second_list_head.next_node
        
        # Move the tail pointer forward
        current_result_tail = current_result_tail.next_node

    # One of the lists is now empty
    # Attach whatever is left of the non-empty list to our result
    # If both are empty, this just attaches None (which is fine)
    current_result_tail.next_node = first_list_head if first_list_head is not None else second_list_head
    
    # Return the first actual node of our result (skip the dummy)
    return dummy_result_head.next_node


def main() -> None:
    """
    Main function to demonstrate the merge_two_lists function with an example.
    """
    # Example: Merge two sorted lists
    # First list: [1, 4, 6, 7, 8]
    # Second list: [2, 3, 5, 9]
    # Merged result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    first_sorted_list = list_to_nodes([1, 4, 6, 7, 8])
    second_sorted_list = list_to_nodes([2, 3, 5, 9])
    
    merged_list_head = merge_two_lists(first_sorted_list, second_sorted_list)
    merged_as_list = nodes_to_list(merged_list_head)
    
    print("Merged sorted list: " + str(merged_as_list))

if __name__ == "__main__":
    main()