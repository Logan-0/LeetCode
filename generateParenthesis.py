class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

    # Follow some simple rules and depth first search to not waste time by pruning bad answers.
        def backtrack(left: int, right: int, current: str) -> str:

    # Rule 1 Don't let left or right go over the maximum parenthesis. We also can't have more right than left ever
            if left > n or right > n or right > left:
                return

    # Rule 2 if we have both reach the maximum just add it no need to investigate furthur
            if left == n and right == n:
                result.append(current)
                return

    # Rule 3 make it happen but always try opening paranthesis first
            backtrack(left + 1, right, current + "(")

            backtrack(left, right+1, current + ")")

        result = []

        backtrack(0,0,"")

        return result

def main() -> None:
    solution = Solution().generateParenthesis(5)
    print(solution)

if __name__ == "__main__":
    main()


