def longest_consecutive_sequence(numbers: list[int]) -> int:
    """
    This function finds the length of the longest sequence of consecutive integers in a list.
    A consecutive sequence means numbers that follow each other without gaps (e.g., 1, 2, 3, 4).
    
    The approach:
    1. Remove duplicate numbers
    2. Sort the numbers in ascending order
    3. Look for sequences where each number is exactly 1 greater than the previous
    
    Args:
        numbers: A list of integers (may contain duplicates and be unsorted)
        
    Returns:
        The length of the longest consecutive sequence
    """
    
    # Initialize counters for tracking sequence lengths
    current_sequence_length = 1
    longest_sequence_length = 1

    # Remove duplicates by converting to a set, then back to a list
    # This ensures we only count each number once
    unique_numbers = list(set(numbers))

    # Sort the numbers so we can check for consecutive sequences
    unique_numbers.sort()

    # Print the sorted unique numbers for educational purposes
    print("Sorted unique numbers:", unique_numbers)

    # Loop through the sorted numbers to find consecutive sequences
    for current_index in range(0, len(unique_numbers) - 1, 1):
        current_number = unique_numbers[current_index]
        next_number = unique_numbers[current_index + 1]
        

        print("Checking: " + str(current_number) + " and " + str(next_number))

        # If the next number is exactly 1 greater than the current number,
        # they are consecutive and part of the same sequence
        if next_number - current_number == 1:
            current_sequence_length += 1

            # If this sequence is longer than any we've seen, update our record
            if current_sequence_length > longest_sequence_length:
                longest_sequence_length = current_sequence_length
        
        # If the numbers are not consecutive, the current sequence ends
        # Reset the counter to start a new sequence
        else:
            current_sequence_length = 1

    return longest_sequence_length

def main() -> None:
    """
    Main function to demonstrate the longest_consecutive_sequence function with an example.
    """
    # Example: Find the longest consecutive sequence in [100, 4, 200, 1, 3, 2]
    # Sorted unique: [1, 2, 3, 4, 100, 200]
    # Consecutive sequences: [1, 2, 3, 4] (length 4), [100] (length 1), [200] (length 1)
    # Longest: [1, 2, 3, 4] with length 4
    solution = longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
    print("Longest consecutive sequence length: " + str(solution))

if __name__ == "__main__":
    main()
