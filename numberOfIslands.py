def num_of_islands(grid: list[list[str]]) -> int:
    """
    This function counts the number of islands in a 2D grid map.
    An island is formed by connecting adjacent lands horizontally or vertically.
    '1' represents land, '0' represents water.
    
    We use a technique called "Depth-First Search" (DFS) to explore each island.
    When we find land ('1'), we explore all connected land and mark it as visited
    by changing it to water ('0'). This way, we don't count the same island twice.
    
    Args:
        grid: A 2D list where '1' is land and '0' is water
        
    Returns:
        The number of islands found
    """
    
    def depth_first_search(row_index: int, column_index: int) -> None:
        """
        This is a recursive helper function that explores an island using DFS.
        It marks all connected land as visited by changing '1' to '0'.
        """
        
        # Mark the current cell as visited by changing it to water
        grid[row_index][column_index] = "0"

        # These represent the four directions: up, right, down, left
        # Each tuple is (row_change, column_change)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Check all four neighboring cells
        for row_change, column_change in directions:
            new_row_index = row_index + row_change
            new_column_index = column_index + column_change

            # Check if the neighbor is within grid bounds and is land
            if (0 <= new_row_index < number_of_rows and 
                0 <= new_column_index < number_of_columns and 
                grid[new_row_index][new_column_index] == "1"):
                # Recursively explore this neighbor
                depth_first_search(new_row_index, new_column_index)

    # Count the number of islands we find
    island_count = 0

    # Get the dimensions of the grid
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])

    # Scan through every cell in the grid
    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            
            # If we find land ('1'), we've discovered a new island
            if grid[row_index][column_index] == "1":
                # Explore the entire island and mark it as visited
                depth_first_search(row_index, column_index)
                island_count += 1

    return island_count


def main() -> None:
    """
    Main function to demonstrate the num_of_islands function with an example.
    """
    # Example grid:
    # 1 1 1 1 0
    # 1 1 0 1 0
    # 1 1 0 0 0
    # 0 0 0 0 0
    # This represents one large island (the connected '1's)
    solution = num_of_islands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ])
    print("Number of islands: " + str(solution))

if __name__ == "__main__":
    main()

    