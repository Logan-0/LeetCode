def rotate_image(matrix: list[list[int]]) -> None:
    """
    Rotates an n x n matrix 90 degrees clockwise, in place.

    The two-step approach (no extra space needed):

    Step 1 -- Transpose:
        Swap matrix[row][col] with matrix[col][row] for every pair where col > row.
        This reflects the matrix along its main diagonal (top-left to bottom-right).

    Step 2 -- Reverse each row:
        Reversing each row after the transpose is mathematically equivalent to
        a 90-degree clockwise rotation.

    Why does this work?
        A 90-degree clockwise rotation sends the element at (row, col) to (col, n-1-row).
        Transpose sends (row, col) to (col, row).
        Then reversing row col gives position (col, n-1-row). These compose correctly.

    Visual example (3x3):
        Original:         After transpose:  After row reversal:
        [1,  2,  3]       [1, 4, 7]         [7, 4, 1]
        [4,  5,  6]  -->  [2, 5, 8]  -->    [8, 5, 2]
        [7,  8,  9]       [3, 6, 9]         [9, 6, 3]

    Args:
        matrix: A square (n x n) list of lists of integers, modified in place

    Returns:
        None -- the matrix is modified directly; nothing is returned

    Time Complexity: O(n^2) -- every element is visited during transpose and reversal
    Space Complexity: O(1) -- all operations are done in place
    """

    matrix_size = len(matrix)

    # Step 1: Transpose -- only visit pairs above the main diagonal (col > row)
    for row_index in range(matrix_size):
        for col_index in range(row_index + 1, matrix_size):
            # Swap the two mirrored positions across the diagonal
            matrix[row_index][col_index], matrix[col_index][row_index] = (
                matrix[col_index][row_index], matrix[row_index][col_index]
            )

    # Step 2: Reverse each row to complete the clockwise rotation
    for row_index in range(matrix_size):
        matrix[row_index].reverse()


def main() -> None:
    """
    Main function to demonstrate rotate_image with a 3x3 and a 4x4 example.
    """
    matrix_three_by_three = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print("3x3 before rotation:")
    for row in matrix_three_by_three:
        print("  " + str(row))

    rotate_image(matrix_three_by_three)

    print("3x3 after 90-degree clockwise rotation:")
    for row in matrix_three_by_three:
        print("  " + str(row))

    print("")

    matrix_four_by_four = [
        [ 5,  1,  9, 11],
        [ 2,  4,  8, 10],
        [13,  3,  6,  7],
        [15, 14, 12, 16],
    ]

    print("4x4 before rotation:")
    for row in matrix_four_by_four:
        print("  " + str(row))

    rotate_image(matrix_four_by_four)

    print("4x4 after 90-degree clockwise rotation:")
    for row in matrix_four_by_four:
        print("  " + str(row))


if __name__ == "__main__":
    main()
