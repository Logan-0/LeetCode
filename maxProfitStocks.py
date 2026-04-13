class Solution:
    def maxProfit(self, dayPriceList: list[int]) -> list[int]:

        profit = 0

        for i in range(len(dayPriceList)-1, 0, -1):
            if dayPriceList[i]  > dayPriceList[i-1]:
                profit += dayPriceList[i] - dayPriceList[i-1]

        return profit
            

def main() -> None:
    solution = Solution().maxProfit([1,6,4,7,3,1,2,4,5,9,0])
    print(solution)

if __name__ == "__main__":
    main()

