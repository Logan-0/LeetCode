def two_sum_brute_force(numbers: list[int], target_sum: int) -> list[int]:
    """
    This function finds two numbers in a list that add up to a target sum.
    It uses a "brute force" approach, which means we check every possible pair.
    This is simple but not the most efficient method for very large lists.
    
    Args:
        numbers: A list of integers to search through
        target_sum: The sum we want to achieve by adding two numbers
        
    Returns:
        A list containing the indices of the two numbers that add up to target_sum,
        or an empty list if no such pair exists
    """
    
    # Loop through each number in the list (using its index)
    for first_index in range(len(numbers)):
        
        # Loop through each number that comes after the first number
        # We start at first_index + 1 to avoid checking the same pair twice
        for second_index in range(first_index + 1, len(numbers)):
            
            # Check if these two numbers add up to our target sum
            if numbers[first_index] + numbers[second_index] == target_sum:
                
                # We found a match! Return the indices of both numbers
                return [first_index, second_index]
    
    # If we checked all pairs and found no match, return an empty list
    return []


def main() -> None:
    """
    Main function to demonstrate the two_sum_brute_force function with an example.
    """
    # Example: Find two numbers that add up to 45
    # In the list [4, 5, 3, 67, 13, 42, 15], the numbers 3 and 42 add up to 45
    # 3 is at index 2, 42 is at index 5
    result = two_sum_brute_force([4, 5, 3, 67, 13, 42, 15], 45)
    print(result)


if __name__ == "__main__":
    main()
