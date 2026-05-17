def binary_search(sorted_numbers: list[int], target: int) -> int:
    """
    Finds the index of a target value in a sorted list using binary search.

    The core idea: because the list is sorted we can eliminate half of the
    remaining candidates with every comparison.

    Algorithm:
    1. Maintain a left and right boundary defining the current search window
    2. Calculate the midpoint of the window
    3. If the middle value equals the target, return that index
    4. If the target is larger than the middle, search the right half
    5. If the target is smaller than the middle, search the left half
    6. If the window shrinks to nothing, the target is not in the list

    Contrast with a linear scan (O(n)): binary search only needs O(log n)
    comparisons because the search space halves every step. On a list of
    one million elements, that is at most about 20 comparisons.

    Args:
        sorted_numbers: A list of integers sorted in ascending order
        target: The value to search for

    Returns:
        The index of target in sorted_numbers, or -1 if target is not present

    Time Complexity: O(log n) -- search space halves with each iteration
    Space Complexity: O(1) -- only a handful of variables needed
    """

    left_boundary = 0
    right_boundary = len(sorted_numbers) - 1

    while left_boundary <= right_boundary:
        # Use this formula to avoid integer overflow (important in other languages)
        middle_index = left_boundary + (right_boundary - left_boundary) // 2
        middle_value = sorted_numbers[middle_index]

        if middle_value == target:
            return middle_index

        elif middle_value < target:
            # Target must be in the right half -- discard everything up to middle
            left_boundary = middle_index + 1

        else:
            # Target must be in the left half -- discard everything from middle onward
            right_boundary = middle_index - 1

    # The search window is empty; the target is not in the list
    return -1


def main() -> None:
    """
    Main function to demonstrate binary_search with a sample sorted list.
    """
    numbers = [-10, -3, 0, 5, 9, 14, 22, 35, 47]

    print("Searching in: " + str(numbers))
    print("")
    print("Index of  9:   " + str(binary_search(numbers, 9)))
    print("Index of -3:   " + str(binary_search(numbers, -3)))
    print("Index of  47:  " + str(binary_search(numbers, 47)))
    print("Index of -10:  " + str(binary_search(numbers, -10)))
    print("Index of  100: " + str(binary_search(numbers, 100)) + "  (not found)")
    print("Index of  1:   " + str(binary_search(numbers, 1)) + "  (not found)")


if __name__ == "__main__":
    main()
