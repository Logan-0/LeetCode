def rob(house_values: list[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. Each
    house has a certain amount of money. Adjacent houses have security systems
    connected -- if you rob two adjacent houses, the alarm triggers.

    Given an array of non-negative integers representing the amount of money in
    each house, return the maximum amount you can rob tonight without triggering
    any alarms.

    LeetCode #198 - House Robber
    Difficulty: Medium
    Pattern: Dynamic Programming

    Example:
        Input:  [1, 2, 3, 1]
        Output: 4   (rob house 1 and house 3: 1 + 3 = 4)

        Input:  [2, 7, 9, 3, 1]
        Output: 12  (rob house 1, 3, and 5: 2 + 9 + 1 = 12)

    Hint: At each house, you choose to rob it (earning its value + best up to
          two houses ago) or skip it (keeping the best up to the previous house).

    Time complexity goal: O(n)
    Space complexity goal: O(1)

    Args:
        house_values: A list of non-negative integers, one per house

    Returns:
        The maximum amount that can be robbed without triggering alarms
    """
    pass


def main() -> None:
    """
    Main function to demonstrate the rob function.
    """
    result = rob([2, 7, 9, 3, 1])
    print("Maximum rob amount for [2,7,9,3,1]: " + str(result))


if __name__ == "__main__":
    main()
