class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}
        
        def recurse(remaining):
            # Base cases
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            # Check memo
            if remaining in memo:
                return memo[remaining]
            
            # Try each coin, find minimum
            min_coins = float('inf')
            for coin in coins:
                result = recurse(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)
            
            # Store and return
            memo[remaining] = min_coins
            return min_coins
        
        result = recurse(amount)
        return result if result != float('inf') else -1



def main() -> None:
    # Example 1: coins=[3,5,7], amount=11
    # Possible: 11 = 5+3+3 (3 coins)
    solution1 = Solution().coinChange([3,5,7], 11)
    print(f"coins=[3,5,7], amount=11 → {solution1} coins")
    
    # Example 2: coins=[3,5,7], amount=4
    # Impossible! Can't make 4 with 3,5,7
    solution2 = Solution().coinChange([3,5,7], 4)
    print(f"coins=[3,5,7], amount=4 → {solution2} (impossible)")
    
    # Example 3: coins=[3,5,7], amount=15
    # Possible: 15 = 5+5+5 (3 coins) or 7+5+3 (3 coins)
    solution3 = Solution().coinChange([3,5,7], 15)
    print(f"coins=[3,5,7], amount=15 → {solution3} coins")
    
    # Example 4: coins=[3,5,7], amount=1
    # Impossible! All coins are too large
    solution4 = Solution().coinChange([3,5,7], 1)
    print(f"coins=[3,5,7], amount=1 → {solution4} (impossible)")

if __name__ == "__main__":
    main()