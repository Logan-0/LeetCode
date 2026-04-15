def length_of_lis(numbers: list[int]) -> int:
    """
    This function finds the length of the longest increasing subsequence in a list.
    A subsequence is a sequence that can be derived from the array by deleting some or no elements
    without changing the order of the remaining elements.
    
    For example, in [1, 4, 2, 6, 3, 13, 20], one increasing subsequence is [1, 2, 3, 13, 20] with length 5.
    The longest increasing subsequence is [1, 4, 6, 13, 20] with length 5.
    
    This uses Dynamic Programming: we calculate the longest subsequence ending at each position.
    
    Args:
        numbers: A list of integers
        
    Returns:
        The length of the longest increasing subsequence
    """
    
    # Special case: if all numbers are the same, the longest increasing subsequence is just 1
    if len(set(numbers)) == 1:
        return 1

    # Special case: if there's only one number, the longest increasing subsequence is 1
    if len(numbers) == 1:
        return 1

    # Create a dynamic programming array where each element represents
    # the length of the longest increasing subsequence ending at that index
    # Initialize all to 1 because each number by itself is a subsequence of length 1
    longest_subsequence_ending_at_index = [1] * len(numbers)

    # For each position in the array (starting from the second element)
    for current_index in range(1, len(numbers)):
        
        # Look at all elements before the current position
        for previous_index in range(current_index):
            
            # If the current number is greater than a previous number,
            # we can extend the subsequence that ended at the previous position
            if numbers[current_index] > numbers[previous_index]:
                
                # Update the longest subsequence ending at current position
                # It's either the current value, or the value from previous position + 1
                longest_subsequence_ending_at_index[current_index] = max(
                    longest_subsequence_ending_at_index[current_index],
                    longest_subsequence_ending_at_index[previous_index] + 1
                )
                
                # Print for educational purposes to see the DP in action
                print("Can extend: index " + str(previous_index) + " (value " + str(numbers[previous_index]) + ") -> index " + str(current_index) + " (value " + str(numbers[current_index]) + ")")

    # The answer is the maximum value in our DP array
    return max(longest_subsequence_ending_at_index)

def main() -> None:
    """
    Main function to demonstrate the length_of_lis function with an example.
    """
    # Example: Find the longest increasing subsequence in [1, 4, 2, 6, 3, 13, 20]
    # One possible LIS: [1, 2, 3, 13, 20] with length 5
    # Another LIS: [1, 4, 6, 13, 20] with length 5
    solution = length_of_lis([1, 4, 2, 6, 3, 13, 20])
    print("Length of longest increasing subsequence: " + str(solution))

if __name__ == "__main__":
    main()