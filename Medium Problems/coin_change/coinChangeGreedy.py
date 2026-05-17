def coin_change_greedy(coin_denominations: list[int], target_amount: int) -> int:
    """
    This function calculates the minimum number of coins needed to make a target amount
    using a "greedy" approach. The greedy approach always picks the largest coin possible
    at each step. This works well for some coin systems (like US coins) but not all.
    
    Think of it like making change: you always start with the largest coin you can use,
    then move to smaller coins until you reach the exact amount.
    
    Args:
        coin_denominations: A list of available coin values (e.g., [1, 2, 5])
        target_amount: The total amount we want to make with coins
        
    Returns:
        The minimum number of coins needed, or -1 if it's impossible
    """
    # Track the total value of coins we've used so far
    current_total = 0
    
    # Sort the coins so we can process them from smallest to largest
    # This helps us find the largest coin that fits
    coin_denominations.sort()
    
    # Count how many coins we've used
    coin_count = 0

    # Special case: if we only have one type of coin and it can't make the amount evenly
    # Then it's impossible (e.g., trying to make 7 cents with only 5-cent coins)
    if len(coin_denominations) == 1 and target_amount % coin_denominations[0] != 0:
        return -1

    # Keep adding coins until we reach or exceed the target amount
    while current_total < target_amount:
        
        # Try coins from largest to smallest (that's why we go backwards through the list)
        for coin_index in range(len(coin_denominations) - 1, -1, -1):
            current_coin_value = coin_denominations[coin_index]
            
            # Keep using this coin as long as it doesn't make us exceed the target
            while current_total + current_coin_value <= target_amount:
                current_total += current_coin_value
                coin_count += 1

                # If we've reached the exact target, we're done!
                if current_total == target_amount:
                    return coin_count
    
    # If we exit the loop without reaching the target, it's impossible
    return -1

def main() -> None:
    """
    Main function to demonstrate the coin_change_greedy function with an example.
    """
    # Example: Make 11 cents with coins 1, 2, 5
    # Greedy approach: 5 + 5 + 1 = 11 (3 coins)
    solution = coin_change_greedy([1, 2, 5], 11)
    print(solution)

if __name__ == "__main__":
    main()