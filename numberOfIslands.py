class Solution:
    def numOfIslands(self, grid: list[list[str]]) -> int:

        def dfs(row: int, col: int) -> None:

            #Sink the island
            grid[row][col] = "0"

            # Get the directional pairs (up, right, down, left)
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:

                #check the neighbors
                # 1. current position plus each pair
                x,y = row + dr, col + dc

                # 2. are the neighbors possible
                if 0 <= x < leftRightBounds and 0 <= y < upLowBounds and grid[x][y] == "1":
                    dfs(x,y)

        islandCount = 0

        #get the bounds
        leftRightBounds = len(grid)
        upLowBounds = len(grid[0])

        for i in range(leftRightBounds):
            for j in range(upLowBounds):
                if(grid[i][j] == "1"):
                    dfs(i,j)
                    islandCount += 1

        return islandCount


def main() -> None:
    solution = Solution().numOfIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    print(solution)

if __name__ == "__main__":
    main()

    