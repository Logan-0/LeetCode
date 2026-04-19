from posix import remove


def is_palindrome(input_string: str) -> bool:
    """
    A phrase is a palindrome if, after converting all uppercase letters to
    lowercase and removing all non-alphanumeric characters, it reads the same
    forward and backward. Alphanumeric characters include letters and digits.

    LeetCode #125 - Valid Palindrome
    Difficulty: Easy
    Pattern: Two Pointers / String

    Example:
        Input:  "A man, a plan, a canal: Panama"
        Output: True   (after filtering: "amanaplanacanalpanama")

        Input:  "race a car"
        Output: False  (after filtering: "raceacar")

    Hint: Use two pointers starting from each end, skipping non-alphanumeric
          characters and comparing the remaining characters case-insensitively.

    Args:
        input_string: A string that may contain letters, digits, and symbols

    Returns:
        True if the string is a valid palindrome, False otherwise
    """
    removeAlphaNumeric = ''.join(filter(str.isalnum,input_string))

    small = removeAlphaNumeric.lower()

    length = len(small)

    print(small)

    for i in range(0,length):
        if (small[i] != small[-i-1]):
            return False

    return True


def main() -> None:
    """
    Main function to demonstrate the is_palindrome function.
    """
    result = is_palindrome("A man, a plan, a canal: Panama")
    print("Is palindrome: " + str(result))


if __name__ == "__main__":
    main()
