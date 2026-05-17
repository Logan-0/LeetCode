def final_prices(prices: list[int]) -> list[int]:
    """
    This function calculates the final price of items after applying discounts.
    For each item, we look for the first item to its right that has a lower or equal price.
    If we find one, we subtract that price from the current item's price as a discount.
    
    Args:
        prices: A list of item prices
        
    Returns:
        The same list with discounts applied
    """
    
    # Get the total number of items in the price list
    number_of_items = len(prices)

    # Loop through each item in the list (using index to track position)
    for current_item_index in range(number_of_items):
        
        # Check if there is at least one item after the current item
        # We can only apply a discount if there's a item to compare with
        if current_item_index + 1 < len(prices):
            
            # Look at all items that come after the current item
            for next_item_index in range(current_item_index + 1, number_of_items):
                
                # If we find an item with a price less than or equal to the current item's price
                # Then we can apply a discount!
                if prices[next_item_index] <= prices[current_item_index]:
                    
                    # Subtract the discount price from the current item's price
                    prices[current_item_index] = prices[current_item_index] - prices[next_item_index]
                    
                    # Once we find the first discount, we stop looking for more discounts
                    # (only the first lower price to the right counts)
                    break
    
    # Return the modified list with discounts applied
    return prices


def main() -> None:
    """
    Main function to demonstrate the final_prices function with an example.
    """
    # Example: Shop with prices [8, 4, 6, 2, 3]
    # - Item at index 0 (price 8): finds price 4 at index 1, so final price = 8 - 4 = 4
    # - Item at index 1 (price 4): finds price 2 at index 3, so final price = 4 - 2 = 2
    # - Item at index 2 (price 6): finds price 2 at index 3, so final price = 6 - 2 = 4
    # - Item at index 3 (price 2): no lower price after it, so final price = 2
    # - Item at index 4 (price 3): no items after it, so final price = 3
    # Result: [4, 2, 4, 2, 3]
    print(final_prices([8, 4, 6, 2, 3]))

if __name__ == "__main__":
    main()