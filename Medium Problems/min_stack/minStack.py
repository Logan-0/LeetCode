def create_min_stack():
    """
    This function creates a special stack that can return the minimum element in O(1) time.
    A regular stack can only give you the top element, but finding the minimum would require
    looking at all elements (O(n) time).
    
    The trick: we maintain TWO stacks:
    1. The main stack that stores all the elements
    2. A "minimum stack" that stores the minimum element at each state
    
    For example, if we push [5, 3, 8]:
    - Main stack: [5, 3, 8]
    - Min stack: [inf, 5, 3, 3]  (at each step, we store the current minimum)
    
    This way, to get the minimum, we just look at the top of the min stack!
    
    Returns:
        A dictionary containing functions to operate on the stack (push, pop, top, get_min)
    """
    
    # This is our main stack - stores all elements in order
    main_stack = []
    
    # This is our minimum stack - stores the minimum at each state
    # We start with infinity as a sentinel value
    minimum_tracking_stack = [float('inf')]

    def push_element(value_to_push: int) -> None:
        """
        Push an element onto the stack and update the minimum tracking.
        
        Args:
            value_to_push: The integer value to push onto the stack
        """
        # Add the value to the main stack
        main_stack.append(value_to_push)
        
        # Add the current minimum to the minimum tracking stack
        # The current minimum is the smaller of: the new value or the previous minimum
        current_minimum = min(value_to_push, minimum_tracking_stack[-1])
        minimum_tracking_stack.append(current_minimum)

    def pop_element() -> None:
        """
        Remove the top element from the stack.
        We also remove the corresponding minimum from the tracking stack.
        """
        main_stack.pop()
        minimum_tracking_stack.pop()

    def peek_top() -> int:
        """
        Get the top element of the stack without removing it.
        
        Returns:
            The value of the top element
        """
        return main_stack[-1]

    def get_minimum() -> int:
        """
        Retrieve the minimum element currently in the stack.
        This happens in O(1) time because we just look at the top of the minimum stack!
        
        Returns:
            The minimum element in the stack
        """
        return minimum_tracking_stack[-1]

    # Return a dictionary with all the stack operations
    # This is a functional approach - we return functions instead of methods
    return {
        'push': push_element,
        'pop': pop_element,
        'top': peek_top,
        'get_min': get_minimum
    }


def main() -> None:
    """
    Main function to demonstrate the create_min_stack function with an example.
    """
    # Create a new minimum stack
    my_stack = create_min_stack()

    # Push elements: 14, 3, 44, 22
    # After each push:
    # Push 14: main=[14], min=[inf, 14], minimum=14
    # Push 3:  main=[14, 3], min=[inf, 14, 3], minimum=3
    # Push 44: main=[14, 3, 44], min=[inf, 14, 3, 3], minimum=3
    # Push 22: main=[14, 3, 44, 22], min=[inf, 14, 3, 3, 3], minimum=3
    my_stack['push'](14)
    my_stack['push'](3)
    my_stack['push'](44)
    my_stack['push'](22)

    # Pop the top element (22)
    # After pop: main=[14, 3, 44], min=[inf, 14, 3, 3], minimum=3
    popped_value = my_stack['pop']()
    print("Popped value: " + str(popped_value))

    # Peek at the top (should be 44)
    top_value = my_stack['top']()
    print("Top value: " + str(top_value))

    # Get the minimum (should be 3)
    minimum_value = my_stack['get_min']()
    print("Minimum value: " + str(minimum_value))

if __name__ == "__main__":
    main()