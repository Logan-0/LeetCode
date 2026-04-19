def longest_palindromic_substring(text: str) -> str:
    """
    Finds the longest contiguous substring of text that reads the same
    forwards and backwards (a palindrome).

    The "expand around center" approach:
    - Every palindrome mirrors around a center point
    - For a string of length n, there are 2n - 1 possible centers:
        * n centers for odd-length palindromes (each character is the center)
        * n - 1 centers for even-length palindromes (each gap between characters)
    - For each center, we expand outward as long as the left and right characters match
    - We keep track of the start index and length of the longest palindrome found

    Example with "babad":
        Center index 0 ('b'): only "b"        length 1
        Center index 1 ('a'): expands to "bab" length 3  <-- new longest
        Center index 2 ('b'): expands to "aba" length 3  (tie, first one kept)
        Center index 3 ('a'): only "a"        length 1
        Center index 4 ('d'): only "d"        length 1
        Result: "bab"

    Args:
        text: The input string to search (may be empty)

    Returns:
        The longest palindromic substring. If there is a tie, the one found
        first (leftmost, then shortest center) is returned.

    Time Complexity: O(n^2) -- n centers, each expansion up to O(n)
    Space Complexity: O(1) -- only index variables are needed
    """

    if len(text) < 2:
        return text

    # Track the start index and length of the longest palindrome found so far
    longest_start_index = 0
    longest_length = 1

    def expand_from_center(left_index: int, right_index: int) -> None:
        """
        Expands outward from a center defined by left_index and right_index,
        updating longest_start_index and longest_length when a longer palindrome
        is found.

        For odd-length palindromes: left_index == right_index (single character center)
        For even-length palindromes: right_index == left_index + 1 (gap between characters)
        """

        nonlocal longest_start_index, longest_length

        while left_index >= 0 and right_index < len(text) and text[left_index] == text[right_index]:
            current_length = right_index - left_index + 1

            if current_length > longest_length:
                longest_start_index = left_index
                longest_length = current_length

            left_index -= 1
            right_index += 1

    for center_index in range(len(text)):
        # Try an odd-length palindrome centered on this character
        expand_from_center(center_index, center_index)

        # Try an even-length palindrome centered on the gap after this character
        expand_from_center(center_index, center_index + 1)

    return text[longest_start_index : longest_start_index + longest_length]


def main() -> None:
    """
    Main function to demonstrate longest_palindromic_substring with examples.
    """
    examples = [
        "babad",
        "cbbd",
        "racecar",
        "abacaba",
        "a",
        "ac",
    ]

    for example in examples:
        result = longest_palindromic_substring(example)
        print("Input: '" + example + "'  ->  Longest palindrome: '" + result + "'")


if __name__ == "__main__":
    main()
