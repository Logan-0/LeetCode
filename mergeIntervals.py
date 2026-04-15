def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    This function merges overlapping intervals. An interval is represented as [start, end].
    Two intervals overlap if one starts before the other ends.
    
    For example, [1,3] and [2,5] overlap because 2 is between 1 and 3.
    They can be merged into [1,5].
    
    The approach:
    1. Sort intervals by their start time
    2. Compare each interval with the previous one
    3. If they overlap, merge them by taking the later end time
    4. If they don't overlap, add the previous interval to our result
    
    Args:
        intervals: A list of intervals, where each interval is [start, end]
        
    Returns:
        A list of merged, non-overlapping intervals
    """
    
    # Sort intervals by their start time (first element of each interval)
    # This ensures overlapping intervals are adjacent
    intervals.sort()

    # This list will store our merged intervals
    merged_intervals = []

    # Initialize with the first interval as our starting point
    current_interval_start, current_interval_end = intervals[0]

    # Process each remaining interval
    for next_interval_start, next_interval_end in intervals[1:]:
        
        # If the current interval ends before the next one starts,
        # they don't overlap. Save the current interval and start a new one.
        if current_interval_end < next_interval_start:
            merged_intervals.append([current_interval_start, current_interval_end])
            current_interval_start, current_interval_end = next_interval_start, next_interval_end
        
        # If they overlap, merge them by extending the end time if needed
        # The new end time is the maximum of both end times
        else:
            current_interval_end = max(current_interval_end, next_interval_end)

    # Don't forget to add the last interval we were working on
    merged_intervals.append([current_interval_start, current_interval_end])

    return merged_intervals

def main() -> None:
    """
    Main function to demonstrate the merge_intervals function with an example.
    """
    # Example: Merge overlapping intervals
    # [1,3] and [2,5] overlap -> merge to [1,5]
    # [6,7] doesn't overlap with [1,5] -> keep separate
    # [9,14] and [10,15] overlap -> merge to [9,15]
    # Result: [[1,5], [6,7], [9,15]]
    solution = merge_intervals([[1, 3], [2, 5], [6, 7], [9, 14], [10, 15]])
    print("Merged intervals: " + str(solution))

if __name__ == "__main__":
    main()