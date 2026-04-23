def max_area(wall_heights: list[int]) -> int:
    """
    You are given n non-negative integers where each represents the height of a
    vertical wall at that position. Find two walls that together with the x-axis
    form a container that can hold the most water. You may not slant the container.

    LeetCode #11 - Container With Most Water
    Difficulty: Medium
    Pattern: Two Pointers

    Example:
        Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
        Output: 49  (walls at index 1 (height 8) and index 8 (height 7):
                     width = 7, height = min(8,7) = 7, area = 49)

        Input:  [1, 1]
        Output: 1

    Hint: Start with the widest possible container (leftmost and rightmost walls).
          Moving the pointer on the shorter wall inward might find a taller wall
          that compensates for the reduced width.

    Time complexity goal: O(n)
    Space complexity goal: O(1)

    Args:
        wall_heights: A list of non-negative integers representing wall heights

    Returns:
        The maximum area of water a container can hold
    """
    if len(wall_heights) == 1:
        return wall_heights[0]

    highestNum = max(wall_heights)

    wall_heights.remove(highestNum)

    nextHighest = max(wall_heights)

    return nextHighest * nextHighest


def main() -> None:
    """
    Main function to demonstrate the max_area function.
    """
    result = max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print("Maximum water area: " + str(result))


if __name__ == "__main__":
    main()
