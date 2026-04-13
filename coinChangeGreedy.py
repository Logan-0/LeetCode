class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        total = 0
        coins.sort()
        count = 0

        # If there is only one coin and we cannot use it to make the total return the -1
        if len(coins) == 1 and amount % coins[0] != 0:
            return -1

        # While we aren't yet at the number we want
        while total < amount:

            # for each coin in the list
            for eachCoin in range(len(coins)-1, -1, -1):

                # If the largest number on the list doesn't go over the target, keep going until it does.
                # up the count each time
                while total + coins[eachCoin] <= amount:
                    total += coins[eachCoin]
                    count += 1

                    # If we reach the amount return the amount of coins we used
                    if total == amount:
                        return count
        
        return -1

def main() -> None:
    solution = Solution().coinChange([1,2,5], 11)
    print(solution)

if __name__ == "__main__":
    main()