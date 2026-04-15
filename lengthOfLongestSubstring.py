def length_of_longest_substring(input_string: str) -> int:
    """
    This function finds the length of the longest substring without repeating characters.
    A substring is a contiguous sequence of characters within the string.
    
    For example, in "abcabcbb", the longest substring without repeating characters is "abc" with length 3.
    In "bbbbb", the longest substring without repeating characters is "b" with length 1.
    
    Args:
        input_string: The string to analyze
        
    Returns:
        The length of the longest substring without repeating characters
    """
    
    # Track the maximum length found so far
    maximum_length = 0

    # Get the length of the input string
    string_length = len(input_string)

    # For each starting position, try to build the longest unique substring
    for start_index in range(string_length):
        
        # Track characters we've seen in the current substring
        characters_seen_so_far = []

        # Try extending the substring from the starting position
        for current_index in range(start_index, string_length):
            current_character = input_string[current_index]
            
            # If this character hasn't been seen yet in this substring
            if current_character not in characters_seen_so_far:
                # Add it to our seen characters
                characters_seen_so_far.append(current_character)
                
                # Update the maximum length if this substring is longer
                current_substring_length = len(characters_seen_so_far)
                maximum_length = max(maximum_length, current_substring_length)
            else:
                # We found a repeating character, stop this substring
                break

    return maximum_length


def main() -> None:
    """
    Main function to demonstrate the length_of_longest_substring function with examples.
    """
    # Example 1: "abcabcbb" -> longest is "abc" with length 3
    result1 = length_of_longest_substring("abcabcbb")
    print("Length of longest substring in 'abcabcbb': " + str(result1))
    
    # Example 2: "bbbbb" -> longest is "b" with length 1
    result2 = length_of_longest_substring("bbbbb")
    print("Length of longest substring in 'bbbbb': " + str(result2))
    
    # Example 3: "pwwkew" -> longest is "wke" with length 3
    result3 = length_of_longest_substring("pwwkew")
    print("Length of longest substring in 'pwwkew': " + str(result3))

if __name__ == "__main__":
    main()