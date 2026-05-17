def exist(board: list[list[str]], word: str) -> bool:
    """
    Given an m x n grid of characters board and a string word, return true if word
    exists in the grid. The word can be constructed from letters of sequentially
    adjacent cells, where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.

    LeetCode #79 - Word Search
    Difficulty: Medium
    Pattern: DFS / Backtracking

    Example:
        Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: True

        Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
        Output: True

    Hint: Use DFS with backtracking. Start from each cell that matches the first
          letter, then explore all 4 directions. Mark cells as visited to avoid reuse.

    Time complexity goal: O(N * 3^L) - N = cells, L = word length
    Space complexity goal: O(L) - recursion depth

    Args:
        board: 2D grid of characters
        word: The word to search for

    Returns:
        True if the word exists in the grid, False otherwise
    """
    pass


def main() -> None:
    """
    Main function to demonstrate exist with examples.
    """
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    result = exist(board, "ABCCED")
    print("Word 'ABCCED' exists: " + str(result))


if __name__ == "__main__":
    main()
