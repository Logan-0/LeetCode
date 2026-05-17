def contains_duplicate(numbers: list[int]) -> bool:
    """
    Given an integer array, return True if any value appears at least twice,
    or False if every element is distinct.

    LeetCode #217 - Contains Duplicate
    Difficulty: Easy
    Pattern: Array / Hash Set

    Example:
        Input:  [1, 2, 3, 1]
        Output: True   (1 appears twice)

        Input:  [1, 2, 3, 4]
        Output: False  (all distinct)

    Hint: Think about what data structure lets you check membership in O(1).

    Args:
        numbers: A list of integers

    Returns:
        True if any value appears at least twice, False if all are distinct
    """
    checkSet = set(numbers)
    if len(checkSet) != len(numbers):
        return True
    else:
        return False


def main() -> None:
    """
    Main function to demonstrate the contains_duplicate function.
    """
    result = contains_duplicate([1, 2, 3, 1])
    print("Contains duplicate [1,2,3,1]: " + str(result))


if __name__ == "__main__":
    main()
