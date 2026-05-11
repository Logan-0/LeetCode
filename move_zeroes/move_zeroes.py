def move_zeroes(nums: list[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining
    the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    LeetCode #283 - Move Zeroes
    Difficulty: Easy
    Pattern: Two Pointers

    Example:
        Input:  nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Input:  nums = [0]
        Output: [0]

    Hint: Use two pointers - one to track the position for the next non-zero
          element, and another to iterate through the array.

    Time complexity goal: O(n)
    Space complexity goal: O(1) - in-place modification

    Args:
        nums: A list of integers (modified in-place)

    Returns:
        None - the array is modified in-place
    """
    pass


def main() -> None:
    """
    Main function to demonstrate move_zeroes with examples.
    """
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print("After moving zeroes: " + str(nums))


if __name__ == "__main__":
    main()
