def search_insert(nums: list[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value, return the index
    if the target is found. If not, return the index where it would be if it were
    inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    LeetCode #35 - Search Insert Position
    Difficulty: Easy
    Pattern: Binary Search

    Example:
        Input:  nums = [1, 3, 5, 6], target = 5
        Output: 2

        Input:  nums = [1, 3, 5, 6], target = 2
        Output: 1

        Input:  nums = [1, 3, 5, 6], target = 7
        Output: 4

    Hint: Use binary search. If target is not found, the left pointer will be at
          the correct insertion position when the loop ends.

    Time complexity goal: O(log n)
    Space complexity goal: O(1)

    Args:
        nums: A sorted array of distinct integers
        target: The value to search for

    Returns:
        The index where target is located, or the index where it would be inserted
    """
    pass


def main() -> None:
    """
    Main function to demonstrate search_insert with examples.
    """
    result = search_insert([1, 3, 5, 6], 5)
    print("Search insert for [1,3,5,6], target=5: " + str(result))


if __name__ == "__main__":
    main()
