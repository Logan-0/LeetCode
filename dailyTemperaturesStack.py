def daily_temperatures_stack(temperature_list: list[int]) -> list[int]:
    """
    This function calculates, for each day, how many days you have to wait until a warmer temperature.
    If there is no future day for which this is possible, the answer is 0 for that day.
    
    This optimized version uses a "monotonic decreasing stack" approach, which runs in O(n) time.
    This is the standard LeetCode solution and is optimal for large input sizes.
    
    How the stack works:
    - The stack stores indices of days with temperatures in decreasing order (top is smallest)
    - When we find a warmer temperature, we pop all days from the stack that are colder
    - For each popped day, we calculate the days waited
    - This ensures each day is pushed and popped at most once, giving O(n) complexity
    
    For example, given temperatures [73, 74, 75, 71, 69, 72, 76, 73]:
    - Day 0 (73): wait 1 day for 74 -> output 1
    - Day 1 (74): wait 1 day for 75 -> output 1
    - Day 2 (75): wait 4 days for 76 -> output 4
    - Day 3 (71): wait 2 days for 72 -> output 2
    - Day 4 (69): wait 1 day for 72 -> output 1
    - Day 5 (72): wait 1 day for 76 -> output 1
    - Day 6 (76): no warmer day -> output 0
    - Day 7 (73): no warmer day -> output 0
    
    Result: [1, 1, 4, 2, 1, 1, 0, 0]
    
    Args:
        temperature_list: A list of daily temperatures
        
    Returns:
        A list where each element is the number of days to wait for a warmer temperature
    """
    
    # Get the total number of days
    number_of_days = len(temperature_list)

    # Initialize the result list with zeros (default: no warmer day found)
    days_until_warmer = [0] * number_of_days

    # This stack will store indices of days that haven't found a warmer day yet
    # The temperatures at these indices are in decreasing order (monotonic decreasing stack)
    # This means: temperature at stack[0] > temperature at stack[1] > temperature at stack[2]...
    days_waiting_for_warmer_temperature = []

    # Iterate through each day once
    for current_day_index in range(number_of_days):
        current_temperature = temperature_list[current_day_index]

        # While the stack is not empty AND the current temperature is warmer than
        # the temperature at the top of the stack
        while (days_waiting_for_warmer_temperature and 
               current_temperature > temperature_list[days_waiting_for_warmer_temperature[-1]]):
            
            # Pop the day index from the stack (this day found its warmer day!)
            day_that_found_warmer_temperature = days_waiting_for_warmer_temperature.pop()

            # Calculate how many days this day waited
            days_until_warmer[day_that_found_warmer_temperature] = current_day_index - day_that_found_warmer_temperature

        # Push the current day index onto the stack
        # We'll look for a warmer day for it in future iterations
        days_waiting_for_warmer_temperature.append(current_day_index)

    return days_until_warmer


def main() -> None:
    """
    Main function to demonstrate the daily_temperatures_stack function with an example.
    """
    # Example: Find days until warmer temperature for each day
    # Temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
    # Expected output: [1, 1, 4, 2, 1, 1, 0, 0]
    result = daily_temperatures_stack([73, 74, 75, 71, 69, 72, 76, 73])
    print("Days until warmer temperature (stack approach): " + str(result))

if __name__ == "__main__":
    main()
