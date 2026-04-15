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


def add_two_numbers(first_list_head: ListNode | None, second_list_head: ListNode | None) -> ListNode | None:
    """
    This function adds two numbers represented as linked lists.
    Each node contains a single digit, and the digits are stored in reverse order.
    For example, the number 123 is stored as 3 -> 2 -> 1.
    
    We add the numbers digit by digit, just like how we do addition on paper.
    We need to handle "carry" - when the sum of two digits is 10 or more.
    
    Args:
        first_list_head: The head of the first number's linked list
        second_list_head: The head of the second number's linked list
        
    Returns:
        The head of a new linked list representing the sum
    """
    
    # Create a dummy head to simplify building the result list
    dummy_result_head = ListNode(0)
    current_result_node = dummy_result_head

    # This tracks any carry from the previous digit addition
    # For example: 7 + 8 = 15, so we write 5 and carry 1 to the next digit
    carry_over = 0

    # Process both lists until we've used all digits from both
    while first_list_head is not None or second_list_head is not None:
        
        # Get the current digit from each list (or 0 if that list is exhausted)
        first_digit = first_list_head.value if first_list_head is not None else 0
        second_digit = second_list_head.value if second_list_head is not None else 0

        # Add the two digits plus any carry from the previous addition
        digit_sum = carry_over + first_digit + second_digit

        # Calculate the new carry (integer division by 10)
        # For example: 15 // 10 = 1 (the carry)
        carry_over = digit_sum // 10

        # The digit to store is the remainder (modulus 10)
        # For example: 15 % 10 = 5 (the digit we write)
        digit_to_store = digit_sum % 10

        # Create a new node for this digit and add it to our result
        current_result_node.next_node = ListNode(digit_to_store)
        current_result_node = current_result_node.next_node

        # Move to the next digit in each list (if available)
        if first_list_head is not None:
            first_list_head = first_list_head.next_node


        if second_list_head is not None:
            second_list_head = second_list_head.next_node

    # If there's still a carry after processing all digits, add it as a new node
    # For example: adding 99 + 1 = 100, we need to add the final 1
    if carry_over > 0:
        current_result_node.next_node = ListNode(carry_over)

    # Return the first actual node of our result (skip the dummy)
    return dummy_result_head.next_node


def main() -> None:
    """
    Main function to demonstrate the add_two_numbers function with an example.
    """
    # Example: Add 182746 (stored as 6 -> 4 -> 7 -> 2 -> 8 -> 1)
    #          to 11111198642 (stored as 2 -> 6 -> 4 -> 8 -> 9 -> 1 -> 1 -> 1 -> 1 -> 1 -> 1)
    # Result should be 11113061388
    
    first_number_list = list_to_nodes([6, 4, 7, 2, 8, 1])
    second_number_list = list_to_nodes([2, 6, 4, 8, 9, 1, 1, 1, 1, 1, 1])
    
    result_list_head = add_two_numbers(first_number_list, second_number_list)
    result_as_list = nodes_to_list(result_list_head)
    
    print("Result of addition (as linked list): " + str(result_as_list))


if __name__ == "__main__":
    main()

        
