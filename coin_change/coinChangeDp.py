def coin_change_dp(coin_denominations: list[int], target_amount: int) -> int:
    """
    This function calculates the minimum number of coins needed to make a target amount.
    It uses "Dynamic Programming" with "memoization" - a technique where we remember
    previously calculated results to avoid doing the same work twice.
    
    Think of it like solving a puzzle: if you need to make 11 cents with coins of 3, 5, 7,
    you can try using each coin and see what's the minimum for the remaining amount.
    
    Args:
        coin_denominations: A list of available coin values (e.g., [3, 5, 7])
        target_amount: The total amount we want to make with coins
        
    Returns:
        The minimum number of coins needed, or -1 if it's impossible
    """
    
    # This dictionary stores our memoized results
    # Key = remaining amount to make, Value = minimum coins needed for that amount
    memoized_results = {}
    
    def calculate_minimum_coins(remaining_amount: int) -> int:
        """
        This is a recursive helper function that calculates the minimum coins
        needed for a specific remaining amount.
        """
        
        # Base case: If we've made exactly the target amount, we used 0 more coins
        if remaining_amount == 0:
            return 0
        
        # Base case: If we've gone below zero, this path is impossible
        if remaining_amount < 0:
            return float('inf')
        
        # Check if we've already solved this sub-problem before
        if remaining_amount in memoized_results:
            return memoized_results[remaining_amount]
        
        # Try each coin denomination to find the minimum
        minimum_coins_needed = float('inf')
        
        for current_coin in coin_denominations:
            # Recursively calculate coins needed after using this coin
            coins_after_using_current = calculate_minimum_coins(remaining_amount - current_coin)
            
            # If this path is valid (not impossible), update our minimum
            if coins_after_using_current != float('inf'):
                minimum_coins_needed = min(minimum_coins_needed, coins_after_using_current + 1)
        
        # Store this result in our memo so we don't have to calculate it again
        memoized_results[remaining_amount] = minimum_coins_needed
        return minimum_coins_needed
    
    # Calculate the result for the full target amount
    final_result = calculate_minimum_coins(target_amount)
    
    # If the result is infinity, it means it's impossible to make the amount
    return final_result if final_result != float('inf') else -1


def main() -> None:
    """
    Main function to demonstrate the coin_change_dp function with multiple examples.
    """
    # Example 1: Can we make 11 with coins 3, 5, 7?
    # Yes: 5 + 3 + 3 = 11 (3 coins)
    solution1 = coin_change_dp([3, 5, 7], 11)
    print("coins=[3,5,7], amount=11 → " + str(solution1) + " coins")
    
    # Example 2: Can we make 4 with coins 3, 5, 7?
    # No: All coins are too large
    solution2 = coin_change_dp([3, 5, 7], 4)
    print("coins=[3,5,7], amount=4 → " + str(solution2) + " (impossible)")
    
    # Example 3: Can we make 15 with coins 3, 5, 7?
    # Yes: 5 + 5 + 5 = 15 (3 coins) or 7 + 5 + 3 = 15 (3 coins)
    solution3 = coin_change_dp([3, 5, 7], 15)
    print("coins=[3,5,7], amount=15 → " + str(solution3) + " coins")
    
    # Example 4: Can we make 1 with coins 3, 5, 7?
    # No: All coins are too large
    solution4 = coin_change_dp([3, 5, 7], 1)
    print("coins=[3,5,7], amount=1 → " + str(solution4) + " (impossible)")

if __name__ == "__main__":
    main()