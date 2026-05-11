def find_min(nums: list[int]) -> int:
    """
    Given an array of integers nums which is sorted in ascending order and then rotated
    some number of times (to the right), find the minimum element in the array.

    LeetCode #153 - Find Minimum in Rotated Sorted Array
    Difficulty: Medium
    Pattern: Binary Search

    Example:
        Input:  nums = [3,4,5,1,2]
        Output: 1

        Input:  nums = [4,5,6,7,0,1,2]
        Output: 0

        Input:  nums = [11,13,15,17]
        Output: 11

    Hint: Use binary search. Compare the middle element with the rightmost element
          to determine which half contains the minimum.

    Time complexity goal: O(log n)
    Space complexity goal: O(1)

    Args:
        nums: A rotated sorted array of unique integers

    Returns:
        The minimum element in the array
    """
    pass


def main() -> None:
    """
    Main function to demonstrate find_min with examples.
    """
    result = find_min([3, 4, 5, 1, 2])
    print("Minimum in [3,4,5,1,2]: " + str(result))


if __name__ == "__main__":
    main()
