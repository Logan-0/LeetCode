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
    # Get the row and column length
    rowLimit, colLimit = len(matrix), len(matrix[0])

    # Associate Directions -> (0,1) Right == (1,0) Down == (0,-1) Left == (-1, 0) Up
    dirs = (0,1,0,-1,0)

    # For each Number in the Matrix mark them as False for not Visited Yet
    visitedNumber = [[False] * colLimit for _ in range(rowLimit)]

    # Initialize and Markers Needed
    currentRow = currentCol = directionInteger = 0

    # Get something to store results
    spiralRes = []

    # For loop through each of the numbers in the matrix
    for number in range(rowLimit * colLimit):

        # Append the current number
        spiralRes.append(matrix[currentRow][currentCol])

        # Mark that cell as visited
        visitedNumber[currentRow][currentCol] = True

        # Calculate the next position
        nextRow, nextCol = currentRow + dirs[directionInteger], currentCol + dirs[directionInteger + 1]

        # If you go past 0 which means either left or top OR you go past either limits which means bottom or right OR the next one is visited in the grid
        if nextRow < 0 or nextRow >= rowLimit or nextCol < 0 or nextCol >= colLimit or visitedNumber[nextRow][nextCol] == True:

            # DirectionInteger = DirectionInteger + 1 Modulo 4
            directionInteger = (directionInteger + 1) % 4
        currentRow += dirs[directionInteger]
        currentCol += dirs[directionInteger + 1]
    return spiralRes

    



def main() -> None:
    """
    Main function to demonstrate the spiral_order function.
    """
    result = spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Spiral order: " + str(result))


if __name__ == "__main__":
    main()
