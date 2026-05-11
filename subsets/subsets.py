def subsets(nums: list[int]) -> list[list[int]]:
    """
    Given an integer array nums of unique elements, return all possible subsets
    (the power set). The solution set must not contain duplicate subsets. Return
    the solution in any order.

    LeetCode #78 - Subsets
    Difficulty: Medium
    Pattern: Backtracking

    Example:
        Input:  nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        Input:  nums = [0]
        Output: [[],[0]]

    Hint: Use backtracking to build subsets incrementally. For each element, you
          can either include it or exclude it in the current subset.

    Time complexity goal: O(N * 2^N) - N = array length
    Space complexity goal: O(N) - recursion depth

    Args:
        nums: An array of unique integers

    Returns:
        All possible subsets (the power set)
    """
    pass


def main() -> None:
    """
    Main function to demonstrate subsets with examples.
    """
    result = subsets([1, 2, 3])
    print("Subsets of [1,2,3]: " + str(result))


if __name__ == "__main__":
    main()
