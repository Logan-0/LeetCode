def max_subarray(numbers: list[int]) -> int:
    """
    Given an integer array, find the contiguous subarray (containing at least
    one number) that has the largest sum and return that sum.

    LeetCode #53 - Maximum Subarray
    Difficulty: Easy
    Pattern: Dynamic Programming / Kadane's Algorithm

    Example:
        Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        Output: 6   (subarray [4, -1, 2, 1] has the largest sum)

        Input:  [-1, -2, -3, -4]
        Output: -1  (single element; take the least negative)

    Hint: At each position, decide whether to extend the current running sum
          or start fresh from the current element.

    Time complexity goal: O(n)
    Space complexity goal: O(1)

    Args:
        numbers: A non-empty list of integers

    Returns:
        The largest sum of any contiguous subarray
    """
    maxArray = current_sum = numbers[0]

    for num in numbers[1:]:
        current_sum = max(current_sum, 0) + num

        maxArray = max(maxArray, current_sum)

    return maxArray


def main() -> None:
    """
    Main function to demonstrate the max_subarray function.
    """
    result = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print("Maximum subarray sum: " + str(result))


if __name__ == "__main__":
    main()
