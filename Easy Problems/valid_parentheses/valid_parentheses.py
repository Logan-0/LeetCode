def is_valid(expression: str) -> bool:
    """
    Determines whether a string of brackets is valid (properly opened and closed).

    A string is valid if:
    1. Every opening bracket has a corresponding closing bracket of the same type
    2. Brackets are closed in the correct order -- the most recently opened must
       be the first to be closed

    The approach uses a stack:
    - When we see an opening bracket, push it onto the stack
    - When we see a closing bracket, the top of the stack must be the matching opener
    - At the end, the stack must be empty (every opener was closed)

    This is the classic stack use-case: tracking things that must match in order.

    Args:
        expression: A string containing only bracket characters: ( ) { } [ ]

    Returns:
        True if the expression is valid, False otherwise

    Time Complexity: O(n) -- single pass through the string
    Space Complexity: O(n) -- stack can hold up to n/2 opening brackets
    """

    # Map each closing bracket to the opening bracket it must be matched with
    matching_opener = {')': '(', '}': '{', ']': '['}

    # Stack tracks the opening brackets we have seen but not yet closed
    open_brackets_stack = []

    for character in expression:

        # If this is a closing bracket, verify the top of the stack matches it
        if character in matching_opener:
            stack_is_empty = len(open_brackets_stack) == 0
            top_does_not_match = (not stack_is_empty and
                                  open_brackets_stack[-1] != matching_opener[character])

            if stack_is_empty or top_does_not_match:
                return False

            # The top matched -- remove it from the stack
            open_brackets_stack.pop()

        else:
            # This is an opening bracket -- push it so we can match it later
            open_brackets_stack.append(character)

    # All openers were matched if and only if the stack is now empty
    return len(open_brackets_stack) == 0


def main() -> None:
    """
    Main function to demonstrate is_valid with a range of examples.
    """
    test_expressions = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "",
        "(((",
    ]

    for expression in test_expressions:
        print("is_valid('" + expression + "') = " + str(is_valid(expression)))


if __name__ == "__main__":
    main()
