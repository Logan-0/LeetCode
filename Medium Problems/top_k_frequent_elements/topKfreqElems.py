def top_k_elements(numbers: list[int], k_most_frequent: int) -> list[int]:
    """
    This function finds the k most frequent elements in a list.
    It counts how many times each number appears, then returns the k numbers
    that appear most frequently.
    
    The approach:
    1. Count the frequency of each number using a dictionary
    2. Create a list of [frequency, number] pairs
    3. Sort by frequency (ascending)
    4. Take the k elements with the highest frequency (from the end)
    
    Args:
        numbers: A list of integers
        k_most_frequent: The number of most frequent elements to return
        
    Returns:
        A list of the k most frequent elements
    """
    
    # Dictionary to store the count of each number
    # Key = number, Value = how many times it appears
    frequency_count = {}

    # Count how many times each number appears
    for current_number in numbers:
        # If we've seen this number before, add 1 to its count
        # If we haven't, start with 0 then add 1
        frequency_count[current_number] = 1 + frequency_count.get(current_number, 0)

    # Create a list of [frequency, number] pairs for sorting
    frequency_number_pairs = []

    for number, count in frequency_count.items():
        frequency_number_pairs.append([count, number])

    # Sort by frequency (ascending order)
    frequency_number_pairs.sort()

    # Print the sorted pairs for educational purposes
    print("Sorted by frequency (ascending):", frequency_number_pairs)

    # Extract the k most frequent elements (from the end of the sorted list)
    most_frequent_elements = []
    while len(most_frequent_elements) < k_most_frequent:
        # pop() removes and returns the last element (highest frequency)
        # We take index 1 to get the number (not the frequency)
        most_frequent_elements.append(frequency_number_pairs.pop()[1])
    
    return most_frequent_elements

def main() -> None:
    """
    Main function to demonstrate the top_k_elements function with an example.
    """
    # Example: Find the 3 most frequent numbers in a long list
    # The number 2 appears many times, 4 appears many times, 5 appears many times
    solution = top_k_elements([1,2,4,2,4,5,5,4,2,2,3,5,6,2,4,3,4,5,2,4,5,3,5,4,6,7,8,9,6,6,4,3,5,6], 3)
    print("Top 3 most frequent elements: " + str(solution))

if __name__ == "__main__":
    main()
