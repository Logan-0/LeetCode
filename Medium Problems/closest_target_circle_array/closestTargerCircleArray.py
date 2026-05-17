from typing import List

def find_closest_target_distance(words: List[str], target_word: str, starting_index: int) -> int:
    """
    This function finds the shortest distance from a starting position to a target word
    in a circular array of words. The array is circular, meaning we can wrap around from
    the end to the beginning.
    
    For example, in the array ["cat", "dog", "fish", "bird"], if we're at index 0 ("cat")
    looking for "bird", the distance is 3 (forward) or 1 (backward wrapping around).
    The shortest distance is 1.
    
    Args:
        words: A list of words in the circular array
        target_word: The word we're searching for
        starting_index: The index where we start searching from
        
    Returns:
        The shortest distance to the target word, or -1 if the target is not found
    """
    
    # If the target word doesn't exist in the array, return -1
    if target_word not in words:
        return -1

    # Get the total number of words in the array
    array_length = len(words)

    # Initialize with the maximum possible distance (the array length)
    minimum_distance = array_length

    # Check each position in the array to find the target word
    for current_index, current_word in enumerate(words):
        
        # If we found the target word at this position
        if current_word == target_word:
            # Calculate the forward distance (absolute difference in indices)
            forward_distance = abs(current_index - starting_index)
            
            # Calculate the backward distance (wrap around the circular array)
            backward_distance = array_length - forward_distance
            
            # Keep the minimum of: forward distance, current minimum, backward distance
            minimum_distance = min(forward_distance, minimum_distance, backward_distance)

    # If minimum_distance is still the array length, we didn't find the target
    return -1 if minimum_distance == array_length else minimum_distance


def main() -> None:
    """
    Main function to demonstrate the find_closest_target_distance function with an example.
    """
    # Example: Find the closest distance to "fish" starting from index 0
    # Words: ["cat", "dog", "fish", "bird", "fish"]
    # Starting at "cat" (index 0), looking for "fish"
    # "fish" appears at index 2 (distance 2) and index 4 (distance 1 backward)
    # Shortest distance is 1
    solution = find_closest_target_distance(["cat", "dog", "fish", "bird", "fish"], "fish", 0)
    print("Shortest distance to target: " + str(solution))


if __name__ == "__main__":
    main()