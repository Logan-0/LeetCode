def generate_parenthesis(number_of_pairs: int) -> list[str]:
    """
    This function generates all valid combinations of parentheses for a given number of pairs.
    It uses a technique called "backtracking" - we try building combinations step by step,
    and if we realize a path won't work, we "backtrack" and try a different path.
    
    Think of it like exploring a maze: at each step, we can either go left (add '(') or right (add ')').
    We keep track of our position and only continue if we're following valid rules.
    
    Args:
        number_of_pairs: The number of pairs of parentheses to generate (e.g., 3 means "((()))")
        
    Returns:
        A list of all valid parenthesis combinations
    """
    
    def backtrack(open_parentheses_count: int, closed_parentheses_count: int, current_string: str) -> None:
        """
        This is a recursive helper function that builds valid parenthesis combinations.
        
        The rules we follow:
        1. We can't have more open or close parentheses than the total pairs
        2. We can never have more close parentheses than open ones (that would be invalid)
        3. We always try adding an open parenthesis first, then a close one
        """
        
        # Rule 1: If we've exceeded the maximum number of parentheses, this path is invalid
        if open_parentheses_count > number_of_pairs or closed_parentheses_count > number_of_pairs:
            return
        
        # Rule 1 continued: We can't have more close than open parentheses
        if closed_parentheses_count > open_parentheses_count:
            return

        # Rule 2: If we've used all open and close parentheses, we found a valid combination!
        if open_parentheses_count == number_of_pairs and closed_parentheses_count == number_of_pairs:
            valid_combinations.append(current_string)
            return

        # Rule 3: First, try adding an open parenthesis
        backtrack(open_parentheses_count + 1, closed_parentheses_count, current_string + "(")

        # Rule 3 continued: Then, try adding a close parenthesis
        backtrack(open_parentheses_count, closed_parentheses_count + 1, current_string + ")")

    # This list will store all the valid combinations we find
    valid_combinations = []

    # Start the backtracking process with no parentheses used yet
    backtrack(0, 0, "")
    
    return valid_combinations

def main() -> None:
    """
    Main function to demonstrate the generate_parenthesis function with an example.
    """
    # Example: Generate all valid combinations with 3 pairs of parentheses
    # Valid combinations: ((())), (()()), (())(), ()(()), ()()()
    solution = generate_parenthesis(5)
    print(solution)

if __name__ == "__main__":
    main()


