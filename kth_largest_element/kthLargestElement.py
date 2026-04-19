import heapq

def create_kth_largest(kth_largest_value: int, initial_numbers: list[int]):
    """
    This function creates a data structure that can efficiently find the k-th largest element
    in a stream of numbers. It uses a "min-heap" which is a special data structure that always
    keeps the smallest element at the top.
    
    The trick: we only keep the k largest numbers in our heap. The smallest of those k numbers
    is at the top of the heap, which is exactly the k-th largest overall!
    
    For example, if k=3 and we have [10, 20, 30, 40, 50], we keep [30, 40, 50] in the heap.
    The top of the heap is 30, which is the 3rd largest number.
    
    Args:
        kth_largest_value: The value of k (e.g., 3 means we want the 3rd largest)
        initial_numbers: A list of numbers to initialize the structure with
        
    Returns:
        A function that can be called to add new numbers and get the current k-th largest
    """
    
    # This is our min-heap - it will always contain at most k elements
    # The smallest element in this heap is the k-th largest overall
    heap_of_largest_numbers = []

    # Add the initial numbers to our heap
    for current_number in initial_numbers:
        
        # Only add this number if we have fewer than k elements,
        # OR if this number is larger than our current k-th largest (the smallest in heap)
        if len(heap_of_largest_numbers) < kth_largest_value or heap_of_largest_numbers[0] < current_number:

            heapq.heappush(heap_of_largest_numbers, current_number)
            
            # If we now have more than k elements, remove the smallest one
            # This keeps only the k largest numbers
            if len(heap_of_largest_numbers) > kth_largest_value:
                heapq.heappop(heap_of_largest_numbers)

    def add_new_number(new_number: int) -> int:
        """
        This function adds a new number to our data structure and returns the current k-th largest.
        
        Args:
            new_number: The new number to add to the stream
            
        Returns:
            The current k-th largest number after adding the new number
        """
        # Same logic as initialization: only add if we have space or if it's larger than current k-th largest
        if len(heap_of_largest_numbers) < kth_largest_value or heap_of_largest_numbers[0] < new_number:
            heapq.heappush(heap_of_largest_numbers, new_number)
            
            # Remove smallest if we exceed k elements
            if len(heap_of_largest_numbers) > kth_largest_value:
                heapq.heappop(heap_of_largest_numbers)
        
        # The k-th largest is now at the top of our heap (the smallest of the k largest)
        return heap_of_largest_numbers[0]

    # Return the function that can be used to add numbers
    return add_new_number


def main() -> None:
    """
    Main function to demonstrate the create_kth_largest function with an example.
    """
    # Example: Create a structure to find the 5th largest number
    # Initialize with [16, 54, 13, 22, 11, 99, 67, 54]
    # The 5 largest are: [54, 54, 67, 99, 11] (after sorting: [11, 54, 54, 67, 99])
    # The 5th largest is 11
    add_number_function = create_kth_largest(5, [16, 54, 13, 22, 11, 99, 67, 54])
    
    # Add 42 - now the 5 largest are [42, 54, 54, 67, 99], so 5th largest is 42
    current_kth_largest = add_number_function(42)
    print("After adding 42, the 5th largest is: " + str(current_kth_largest))
    
    # Add 55 - now the 5 largest are [54, 54, 55, 67, 99], so 5th largest is 54
    current_kth_largest = add_number_function(55)
    print("After adding 55, the 5th largest is: " + str(current_kth_largest))

if __name__ == "__main__":
    main()