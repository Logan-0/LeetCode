def daily_temperatures(temperature_list: list[int]) -> list[int]:
    """
    This function calculates, for each day, how many days you have to wait until a warmer temperature.
    If there is no future day for which this is possible, the answer is 0 for that day.
    
    This version uses forward iteration with a hash map (dictionary), similar to twoSumOnePassHash.
    We maintain a dictionary mapping temperatures to lists of indices where they occur.
    For each day, we look for warmer temperatures that have appeared after it.
    
    Time complexity: O(n * unique_temperatures) - can be better than O(n²) depending on input
    This is simpler than the stack approach and uses forward iteration.
    
    How it works:
    1. First pass: Build a dictionary mapping each temperature to all indices where it appears
    2. Second pass: For each day, look through all warmer temperatures in the dictionary
    3. Find the first occurrence of a warmer temperature that comes after the current day
    4. Calculate the days waited
    
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

    # Dictionary to store all indices where each temperature appears
    # Key = temperature value, Value = list of indices where this temperature occurs
    temperature_to_indices = {}

    # First pass: Build the dictionary with all temperature indices
    for day_index, current_temperature in enumerate(temperature_list):

        if current_temperature not in temperature_to_indices:
            temperature_to_indices[current_temperature] = []

        temperature_to_indices[current_temperature].append(day_index)

    # Second pass: For each day, find the first warmer day
    for current_day_index in range(number_of_days):

        current_temperature = temperature_list[current_day_index]

        # Track the closest warmer day found so far
        closest_warmer_day_index = float('inf')

        # Check all temperatures warmer than the current temperature
        for warmer_temperature in range(current_temperature + 1, 101):

            # If this warmer temperature exists in our dictionary
            if warmer_temperature in temperature_to_indices:

                # Look through all indices where this temperature appears
                for warmer_day_index in temperature_to_indices[warmer_temperature]:

                    # We only care about indices that come AFTER the current day
                    if warmer_day_index > current_day_index:

                        # Keep track of the closest (minimum) index
                        closest_warmer_day_index = min(closest_warmer_day_index, warmer_day_index)
                        
                        # Once we find one, we can stop checking this temperature
                        break

        # If we found a warmer day, calculate the days waited
        if closest_warmer_day_index != float('inf'):
            days_until_warmer[current_day_index] = closest_warmer_day_index - current_day_index

    return days_until_warmer

def main() -> None:
    """
    Main function to demonstrate the daily_temperatures function with an example.
    """
    # Example: Find days until warmer temperature for each day
    # Temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
    # Expected output: [1, 1, 4, 2, 1, 1, 0, 0]
    result = daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print("Days until warmer temperature: " + str(result))

if __name__ == "__main__":
    main()

