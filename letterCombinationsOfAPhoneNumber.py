def combinations_of_phone_number(phone_digits: str) -> list[str]:
    """
    This function generates all possible letter combinations for a phone number.
    On a phone keypad, each number (2-9) is associated with 3-4 letters.
    For example, 2 is "abc", 3 is "def", etc.
    
    This function takes a string of digits and returns all possible letter combinations.
    
    Args:
        phone_digits: A string of digits (e.g., "23" for numbers 2 and 3)
        
    Returns:
        A list of all possible letter combinations
    """
    
    # This list maps each digit to its corresponding letters on a phone keypad
    # Index 0 and 1 are empty because those keys don't have letters
    phone_keypad_mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    # Start with an empty string as our base combination
    current_combinations = [""]
    
    # Process each digit in the phone number one at a time
    for current_digit in phone_digits:
        
        # Get the letters that correspond to this digit
        letters_for_this_digit = phone_keypad_mapping[int(current_digit)]
        
        # For each existing combination, add each possible letter
        # This creates all new combinations by extending the old ones
        # Example: if we have ["a", "b"] and adding "c", "d", we get ["ac", "ad", "bc", "bd"]
        new_combinations = []

        for existing_combination in current_combinations:

            for letter_to_add in letters_for_this_digit:
                
                new_combinations.append(existing_combination + letter_to_add)
        
        # Update our list with the new combinations
        current_combinations = new_combinations

    return current_combinations

def main() -> None:
    """
    Main function to demonstrate the combinations_of_phone_number function with an example.
    """
    # Example: The digits "2475" correspond to:
    # 2 -> "abc"
    # 4 -> "ghi"
    # 7 -> "pqrs"
    # 5 -> "jkl"
    # This generates many combinations like "agpj", "agpk", "agpl", etc.
    solution = combinations_of_phone_number("2475")
    print(solution)

if __name__ == "__main__":
    main()