def permute(nums: list[int]) -> list[list[int]]:
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.

    LeetCode #46 - Permutations
    Difficulty: Medium
    Pattern: Backtracking

    Example:
        Input:  nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        Input:  nums = [0,1]
        Output: [[0,1],[1,0]]

    Hint: Use backtracking to build permutations. Swap elements to generate
          different arrangements, or use a visited set to track used elements.

    Time complexity goal: O(N * N!) - N = array length
    Space complexity goal: O(N) - recursion depth

    Args:
        nums: An array of distinct integers

    Returns:
        All possible permutations
    """
    pass


def main() -> None:
    """
    Main function to demonstrate permute with examples.
    """
    result = permute([1, 2, 3])
    print("Permutations of [1,2,3]: " + str(result))


if __name__ == "__main__":
    main()
