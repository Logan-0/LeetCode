def verify_dictionary(words: list[str], alien_alphabet_order: str) -> bool:
    """
    This function verifies if a list of words is sorted according to an alien alphabet.
    In an alien language, the letters might be in a different order than English.
    We need to check if the words are in the correct order based on this alien alphabet.
    
    The approach:
    1. Create a mapping from each letter to its position in the alien alphabet
    2. Compare words character by character at each position
    3. If at any position, a word has a letter that should come after the next word's letter,
       the dictionary is not sorted correctly
    
    Args:
        words: A list of words to check
        alien_alphabet_order: The order of letters in the alien alphabet
        
    Returns:
        True if the words are sorted correctly according to the alien alphabet, False otherwise
    """
    
    # Create a dictionary that maps each character to its position in the alien alphabet
    # For example, if order is "hlabcdefgijkmnopqrstuvwxyz", then 'h' maps to 0, 'l' maps to 1, etc.
    alien_alphabet_mapping = {character: position for position, character in enumerate(alien_alphabet_order)}

    # Check each character position (up to 7 characters since that's a reasonable word length limit)
    for character_position in range(7):
        
        # This variable tracks the position value of the previous word's character at this position
        # Start with -1 (smaller than any valid position)
        previous_word_character_position = -1

        # This flag tracks if all words have different characters at this position
        # If they're all different, we can determine the order definitively
        all_words_different_at_this_position = True

        # Compare each word at this character position
        for current_word in words:
            
            # If the current word is shorter than the position we're checking,
            # treat it as having a value of -1 (smaller than any actual letter)
            if character_position >= len(current_word):
                current_word_character_position = -1
            else:
                # Get the position of this character in the alien alphabet
                current_word_character_position = alien_alphabet_mapping[current_word[character_position]]

            # If the previous word's character has a higher position value than the current word's,
            # that means the previous word should come AFTER the current word in the alien alphabet
            # This violates the sorted order, so the dictionary is invalid
            if previous_word_character_position > current_word_character_position:
                return False

            # If two words have the same character at this position, we can't determine order yet
            # We need to check the next character position
            if previous_word_character_position == current_word_character_position:
                all_words_different_at_this_position = False

            # Update the previous value for the next iteration
            previous_word_character_position = current_word_character_position

        # If all words have different characters at this position, we've determined the order
        # No need to check further positions
        if all_words_different_at_this_position:
            return True

    # If we've checked all positions and haven't found a violation, the dictionary is valid
    return True

def main() -> None:
    """
    Main function to demonstrate the verify_dictionary function with an example.
    """
    # Example: Check if words are sorted according to alien alphabet "hlabcdefgijkmnopqrstuvwxyz"
    # In this alien alphabet, 'h' comes first, then 'l', then 'a', 'b', 'c', etc.
    words_to_check = ["app", "apple", "application", "appeal", "appear", "apprehend"]
    alien_alphabet = "hlabcdefgijkmnopqrstuvwxyz"
    
    solution = verify_dictionary(words_to_check, alien_alphabet)
    print("Are the words sorted correctly according to the alien alphabet? " + str(solution))

if __name__ == "__main__":
    main()

