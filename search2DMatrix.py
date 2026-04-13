class Solution:

    def search2D(self, matrix: list[list[int]], target: int):

        if len(matrix) < 1:
            return False

        for anyRow in matrix:
            if target in anyRow:
                return True

        return False
    
def main() -> None:
    solution = Solution().search2D([[2,7,13,11],[4,0,15,1],[3,14,6,5]], 8)
    print(solution)
    solution = Solution().search2D([[2,7,13,11],[4,0,15,1],[3,14,6,5]], 5)
    print(solution)

if __name__ == "__main__":
    main()

