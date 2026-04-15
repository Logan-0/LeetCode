def search_2d(matrix: list[list[int]], target_value: int) -> bool:
    """
    This function searches for a target value in a 2D matrix.
    It checks each row to see if the target value is present.
    
    This is a simple linear search approach. For each row, we check if the target
    is in that row using Python's 'in' operator.
    
    Args:
        matrix: A 2D list of integers
        target_value: The value we're searching for
        
    Returns:
        True if the target is found, False otherwise
    """
    
    # If the matrix is empty, we can't find anything
    if len(matrix) < 1:
        return False

    # Check each row in the matrix
    for current_row in matrix:
        # If the target value is in this row, we found it!
        if target_value in current_row:
            return True

    # If we've checked all rows and didn't find the target, it's not in the matrix
    return False

def main() -> None:
    """
    Main function to demonstrate the search_2d function with examples.
    """
    # Example matrix:
    # [2, 7, 13, 11]
    # [4, 0, 15, 1]
    # [3, 14, 6, 5]
    
    # Search for 8 (not in matrix)
    solution1 = search_2d([[2, 7, 13, 11], [4, 0, 15, 1], [3, 14, 6, 5]], 8)
    print("Is 8 in the matrix? " + str(solution1))
    
    # Search for 5 (in the matrix, last row)
    solution2 = search_2d([[2, 7, 13, 11], [4, 0, 15, 1], [3, 14, 6, 5]], 5)
    print("Is 5 in the matrix? " + str(solution2))

if __name__ == "__main__":
    main()

