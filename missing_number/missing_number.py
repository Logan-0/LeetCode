def missing_number(numbers: list[int]) -> int:
    """
    Given an array of n distinct numbers in the range [0, n], return the only
    number in that range that is missing from the array.

    LeetCode #268 - Missing Number
    Difficulty: Easy
    Pattern: Array / Math

    Example:
        Input:  [3, 0, 1]
        Output: 2   (the range is [0,1,2,3]; 2 is missing)

        Input:  [9, 6, 4, 2, 3, 5, 7, 0, 1]
        Output: 8

    Hint: The sum of integers from 0 to n is n*(n+1)/2. Compare that with the
          actual sum of the array to find the missing value.

    Time complexity goal: O(n)
    Space complexity goal: O(1)

    Args:
        numbers: A list of n distinct integers in the range [0, n]

    Returns:
        The one missing integer from the range [0, n]
    """
    sortedArr = sorted(numbers)
    length = len(sortedArr)

    if(sortedArr[0] != 0):
        return 0

    if len(sortedArr) == 1:
        return 1

    for i in range(0,length):
        if (i != sortedArr[i]):
            return i
        if i == length-1:
            return i+1


def main() -> None:
    """
    Main function to demonstrate the missing_number function.
    """
    result = missing_number([3, 0, 1])
    print("Missing number in [3,0,1]: " + str(result))


if __name__ == "__main__":
    main()
