def sort_colors(nums: list[int]) -> None:
    """
    Given an array nums with n objects colored red, white, or blue, sort them in-place
    so that objects of the same color are adjacent, with the colors in the order red,
    white, and blue. We will use the integers 0, 1, and 2 to represent the color red,
    white, and blue, respectively.

    You must solve this problem without using the library's sort function.

    LeetCode #75 - Sort Colors
    Difficulty: Medium
    Pattern: Two Pointers / Dutch National Flag

    Example:
        Input:  nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]

        Input:  nums = [2,0,1]
        Output: [0,1,2]

    Hint: Use the Dutch National Flag algorithm with three pointers: low, mid, and high.
          Maintain invariants: [0, low-1] = 0s, [low, mid-1] = 1s, [high+1, end] = 2s

    Time complexity goal: O(n)
    Space complexity goal: O(1) - in-place

    Args:
        nums: A list of integers containing only 0, 1, and 2 (modified in-place)

    Returns:
        None - the array is modified in-place
    """
    pass


def main() -> None:
    """
    Main function to demonstrate sort_colors with examples.
    """
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    print("After sorting colors: " + str(nums))


if __name__ == "__main__":
    main()
