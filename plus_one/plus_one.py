def plus_one(digits: list[int]) -> list[int]:
    """
    You are given a large integer represented as an integer array digits, where
    each digits[i] is the ith digit of the integer. The digits are ordered from
    most significant to least significant in left-to-right order. The large integer
    does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    LeetCode #66 - Plus One
    Difficulty: Easy
    Pattern: Array / Math

    Example:
        Input:  digits = [1,2,3]
        Output: [1,2,4]

        Input:  digits = [4,3,2,1]
        Output: [4,3,2,2]

        Input:  digits = [9]
        Output: [1,0]

    Hint: Process from right to left, handling carry. If all digits are 9,
          you'll need to add a new digit at the front.

    Time complexity goal: O(n)
    Space complexity goal: O(1) - not counting output array

    Args:
        digits: A list of digits representing a large integer

    Returns:
        The list of digits representing the integer plus one
    """
    pass


def main() -> None:
    """
    Main function to demonstrate plus_one with examples.
    """
    result = plus_one([1, 2, 3])
    print("Plus one of [1,2,3]: " + str(result))


if __name__ == "__main__":
    main()
