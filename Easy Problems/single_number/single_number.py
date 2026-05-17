def single_number(numbers: list[int]) -> int:
    """
    Given a non-empty array of integers where every element appears twice except
    for one, find that single one.

    LeetCode #136 - Single Number
    Difficulty: Easy
    Pattern: Bit Manipulation

    Example:
        Input:  [2, 2, 1]
        Output: 1

        Input:  [4, 1, 2, 1, 2]
        Output: 4

        Input:  [1]
        Output: 1

    Hint: XOR (^) has the property that a ^ a = 0 and a ^ 0 = a.
          If you XOR all numbers together, pairs cancel out, leaving the single number.

    Time complexity goal: O(n)
    Space complexity goal: O(1)

    Args:
        numbers: A non-empty array of integers where every element appears twice
                 except for one

    Returns:
        The single element that appears only once
    """
    pass


def main() -> None:
    """
    Main function to demonstrate single_number with examples.
    """
    result = single_number([2, 2, 1])
    print("Single number in [2,2,1]: " + str(result))


if __name__ == "__main__":
    main()
