def can_jump(jump_lengths: list[int]) -> bool:
    """
    You are given an integer array where each element represents your maximum
    jump length from that position. Starting at index 0, determine if you can
    reach the last index.

    LeetCode #55 - Jump Game
    Difficulty: Medium
    Pattern: Greedy

    Example:
        Input:  [2, 3, 1, 1, 4]
        Output: True   (jump 1 step to index 1, then 3 steps to the end)

        Input:  [3, 2, 1, 0, 4]
        Output: False  (every path leads to index 3 where the jump is 0)

    Hint: Track the furthest index you can currently reach. At each position,
          update that furthest index. If you ever reach a position beyond
          the furthest reachable index, you are stuck.

    Time complexity goal: O(n)
    Space complexity goal: O(1)

    Args:
        jump_lengths: A list of non-negative integers representing max jump lengths

    Returns:
        True if the last index is reachable from index 0, False otherwise
    """
    pass


def main() -> None:
    """
    Main function to demonstrate the can_jump function.
    """
    result = can_jump([2, 3, 1, 1, 4])
    print("Can jump [2,3,1,1,4]: " + str(result))


if __name__ == "__main__":
    main()
