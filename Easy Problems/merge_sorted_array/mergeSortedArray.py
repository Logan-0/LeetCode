def merge_sorted_array(first_array: list[int], first_array_length: int, second_array: list[int], second_array_length: int) -> list[int]:
    """
    This function merges two sorted arrays into one sorted array.
    The first array has extra space at the end to hold the second array's elements.
    We merge from the end backwards to avoid overwriting elements we haven't processed yet.
    
    Think of it like merging two decks of cards that are already sorted:
    You look at the top card of each deck and pick the larger one, placing it at the end.
    
    Args:
        first_array: The first sorted array with extra space at the end
        first_array_length: The number of actual elements in the first array
        second_array: The second sorted array to merge in
        second_array_length: The number of elements in the second array
        
    Returns:
        The merged sorted array (modifies first_array in place)
    """
    
    # Index of the last actual element in the first array
    first_array_last_valid_index = first_array_length - 1
    
    # Index of the last element in the second array
    second_array_last_index = second_array_length - 1
    
    # Index where we should place the next largest element (at the end of the combined array)
    merged_array_last_position = first_array_length + second_array_length - 1

    # Keep merging while there are still elements in the second array to process
    while second_array_last_index >= 0:
        
        # If there are still elements in the first array and the current element
        # from the first array is larger than the current element from the second array
        if first_array_last_valid_index >= 0 and first_array[first_array_last_valid_index] > second_array[second_array_last_index]:
            # Place the larger element (from first array) at the current position
            first_array[merged_array_last_position] = first_array[first_array_last_valid_index]
            first_array_last_valid_index -= 1
        else:
            # Place the larger element (from second array) at the current position
            first_array[merged_array_last_position] = second_array[second_array_last_index]
            second_array_last_index -= 1

        # Move to the next position (going backwards)
        merged_array_last_position -= 1

    return first_array


def main() -> None:
    """
    Main function to demonstrate the merge_sorted_array function with an example.
    """
    # Example: Merge [1, 3, 4, 5] with [2, 4, 7]
    # The first array has extra space: [1, 3, 4, 5, 0, 0, 0]
    # After merging: [1, 2, 3, 4, 4, 5, 7]
    solution = merge_sorted_array([1, 3, 4, 5, 0, 0, 0], 4, [2, 4, 7], 3)
    print("Merged array: " + str(solution))

if __name__ == "__main__":
    main()