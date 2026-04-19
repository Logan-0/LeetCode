def spiral_order(matrix: list[list[int]]) -> list[int]:
    """
    Given an m x n matrix, return all elements of the matrix in spiral order,
    starting from the top-left and moving right, then down, then left, then up,
    repeating inward until all elements have been visited.

    LeetCode #54 - Spiral Matrix
    Difficulty: Medium
    Pattern: Matrix / Simulation

    Example:
        Input:  [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

        Input:  [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
        Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    Hint: Maintain four boundaries (top, bottom, left, right). Traverse each
          edge of the current boundary, then shrink that boundary inward and
          change direction.

    Args:
        matrix: A non-empty m x n matrix of integers

    Returns:
        All elements of the matrix collected in spiral order
    """
    pass


def main() -> None:
    """
    Main function to demonstrate the spiral_order function.
    """
    result = spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Spiral order: " + str(result))


if __name__ == "__main__":
    main()
