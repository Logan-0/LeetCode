def max_profit(daily_stock_prices: list[int]) -> int:
    """
    This function calculates the maximum profit you can make by buying and selling stock
    multiple times. You can buy and sell on the same day, but you must sell before buying again.
    
    The strategy is simple: whenever the price goes up from one day to the next,
    we buy the day before and sell the next day to capture that profit.
    This works because we can make as many transactions as we want.
    
    Args:
        daily_stock_prices: A list of stock prices for consecutive days
        
    Returns:
        The maximum profit achievable
    """
    
    # Track the total profit accumulated from all profitable transactions
    total_profit = 0

    # Loop through the prices backwards (from the last day towards the first)
    # We compare each day's price with the previous day's price
    for current_day_index in range(len(daily_stock_prices) - 1, 0, -1):
        current_day_price = daily_stock_prices[current_day_index]
        previous_day_price = daily_stock_prices[current_day_index - 1]
        
        # If today's price is higher than yesterday's, we can make a profit
        # by buying yesterday and selling today
        if current_day_price > previous_day_price:
            profit_from_this_transaction = current_day_price - previous_day_price
            total_profit += profit_from_this_transaction

    return total_profit

def main() -> None:
    """
    Main function to demonstrate the max_profit function with an example.
    """
    # Example: Stock prices over 11 days: [1,6,4,7,3,1,2,4,5,9,0]
    # Profitable transactions:
    # - Buy at 1, sell at 6: profit = 5
    # - Buy at 4, sell at 7: profit = 3
    # - Buy at 1, sell at 2: profit = 1
    # - Buy at 2, sell at 4: profit = 2
    # - Buy at 4, sell at 5: profit = 1
    # - Buy at 5, sell at 9: profit = 4
    # Total profit = 5 + 3 + 1 + 2 + 1 + 4 = 16
    solution = max_profit([1, 6, 4, 7, 3, 1, 2, 4, 5, 9, 0])
    print("Maximum profit: " + str(solution))

if __name__ == "__main__":
    main()

