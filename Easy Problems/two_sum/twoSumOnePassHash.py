def two_sum_one_pass_hash(numbers: list[int], target_sum: int) -> list[int]:
    """
    This function finds two numbers in a list that add up to a target sum.
    It uses a "hash map" (dictionary) to store numbers we've seen and their indices.
    This allows us to find the answer in just one pass through the list!
    
    The approach:
    1. For each number, calculate what number we need (complement = target - current)
    2. Check if we've already seen that complement in our dictionary
    3. If yes, we found our pair! Return both indices
    4. If no, add the current number to the dictionary and continue
    
    This is much faster than the brute force approach for large lists.
    
    Args:
        numbers: A list of integers to search through
        target_sum: The sum we want to achieve by adding two numbers
        
    Returns:
        A list containing the indices of the two numbers that add up to target_sum,
        or an empty list if no such pair exists
    """
    
    # Dictionary to store numbers we've seen and their indices
    # Key = the number, Value = the index where it appears
    numbers_seen_so_far = {}

    # Loop through each number in the list with its index
    for current_index, current_number in enumerate(numbers):
        
        # Calculate the complement: the number we need to reach the target
        needed_number = target_sum - current_number

        # Check if we've already seen the number we need
        if needed_number in numbers_seen_so_far:
            # We found a pair! Return the index of the needed number and current index
            return [numbers_seen_so_far[needed_number], current_index]

        # If we haven't found a pair yet, store this number and its index
        numbers_seen_so_far[current_number] = current_index
    
    # If we've gone through all numbers and found no pair, return empty list
    return []

def main() -> None:
    """
    Main function to demonstrate the two_sum_one_pass_hash function with an example.
    """
    # Example: Find two numbers that add up to 45
    # In the list [4, 5, 3, 67, 13, 42, 15], the numbers 3 and 42 add up to 45
    # 3 is at index 2, 42 is at index 5
    result = two_sum_one_pass_hash([4, 5, 3, 67, 13, 42, 15], 45)
    print("Indices of numbers that add to 45: " + str(result))

if __name__ == "__main__":
    main()
