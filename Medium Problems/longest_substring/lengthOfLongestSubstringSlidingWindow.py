def length_of_longest_substring_sliding_window(input_string: str) -> int:
    """
    This function finds the length of the longest substring without repeating characters.
    This version uses the "sliding window" technique, which is the optimal O(n) solution.
    
    The sliding window approach:
    - Maintain a window [left, right] that contains only unique characters
    - Expand the window by moving the right pointer forward
    - If a duplicate is found, shrink the window from the left until unique again
    - Each character is added and removed from the set at most once
    
    For example, in "abcabcbb", the longest substring without repeating characters is "abc" with length 3.
    In "bbbbb", the longest substring without repeating characters is "b" with length 1.
    
    Time complexity: O(n) - each character is processed at most twice
    Space complexity: O(min(n, alphabet_size)) - the set stores at most the alphabet size
    
    Args:
        input_string: The string to analyze
        
    Returns:
        The length of the longest substring without repeating characters
    """
    
    # Left pointer - marks the start of our current window
    left_pointer = 0
    
    # Set to track characters currently in our window
    characters_in_current_window = set()
    
    # Track the maximum window size found so far
    maximum_window_length = 0
    
    # Right pointer expands the window by moving forward through the string
    for right_pointer in range(len(input_string)):
        
        current_character = input_string[right_pointer]
        
        # If the current character is already in our window, we have a duplicate
        # Shrink the window from the left until the duplicate is removed
        while current_character in characters_in_current_window:

            # Remove the character at the left pointer from our set
            character_to_remove = input_string[left_pointer]
            characters_in_current_window.remove(character_to_remove)
            
            # Move the left pointer forward to shrink the window
            left_pointer += 1
        
        # Add the current character to our set
        characters_in_current_window.add(current_character)
        
        # Calculate the current window size and update maximum if needed
        # Window size = right - left + 1 (both pointers are inclusive)
        current_window_size = right_pointer - left_pointer + 1
        maximum_window_length = max(maximum_window_length, current_window_size)
    
    return maximum_window_length


def main() -> None:
    """
    Main function to demonstrate the length_of_longest_substring_sliding_window function with examples.
    """
    # Example 1: "abcabcbb" -> longest is "abc" with length 3
    result1 = length_of_longest_substring_sliding_window("abcabcbb")
    print("Length of longest substring in 'abcabcbb': " + str(result1))
    
    # Example 2: "bbbbb" -> longest is "b" with length 1
    result2 = length_of_longest_substring_sliding_window("bbbbb")
    print("Length of longest substring in 'bbbbb': " + str(result2))
    
    # Example 3: "pwwkew" -> longest is "wke" with length 3
    result3 = length_of_longest_substring_sliding_window("pwwkew")
    print("Length of longest substring in 'pwwkew': " + str(result3))
    
    # Example 4: "" (empty string) -> longest is "" with length 0
    result4 = length_of_longest_substring_sliding_window("")
    print("Length of longest substring in '': " + str(result4))

if __name__ == "__main__":
    main()
