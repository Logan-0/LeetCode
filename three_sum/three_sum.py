def three_sum(numbers: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets in the list whose values sum to zero.

    Brute force would check every combination of three elements: O(n^3).
    The optimized approach brings this down to O(n^2) using sorting and
    the two-pointer technique.

    Algorithm:
    1. Sort the list so that the two-pointer scan is possible
    2. For each element at position anchor_index (the "anchor" value):
       a. Skip it if it is a duplicate of the previous anchor (avoid duplicate triplets)
       b. If the anchor is already positive, no triplet can sum to zero (break early)
       c. Place a left pointer just after the anchor and a right pointer at the end
       d. Move the pointers inward based on whether the current sum is too small or too large
       e. When a valid triplet is found, skip over any duplicate values on both sides

    Args:
        numbers: A list of integers (may contain duplicates, in any order)

    Returns:
        A list of all unique triplets [a, b, c] where a + b + c == 0.
        Each triplet is sorted in ascending order.

    Time Complexity: O(n^2) -- O(n log n) sort + O(n) outer loop * O(n) two-pointer scan
    Space Complexity: O(1) extra -- not counting the output list
    """

    # Sort so we can use two pointers and detect duplicates easily
    sorted_numbers = sorted(numbers)
    found_triplets = []

    for anchor_index in range(len(sorted_numbers) - 2):
        anchor_value = sorted_numbers[anchor_index]

        # Skip duplicate anchor values to prevent duplicate triplets in the output
        if anchor_index > 0 and anchor_value == sorted_numbers[anchor_index - 1]:
            continue

        # If the smallest remaining value is positive, all sums will be positive -- stop
        if anchor_value > 0:
            break

        left_pointer = anchor_index + 1
        right_pointer = len(sorted_numbers) - 1

        while left_pointer < right_pointer:
            current_sum = anchor_value + sorted_numbers[left_pointer] + sorted_numbers[right_pointer]

            if current_sum == 0:
                found_triplets.append([anchor_value,
                                       sorted_numbers[left_pointer],
                                       sorted_numbers[right_pointer]])

                # Skip over duplicate values on the left side
                while (left_pointer < right_pointer and
                       sorted_numbers[left_pointer] == sorted_numbers[left_pointer + 1]):
                    left_pointer += 1

                # Skip over duplicate values on the right side
                while (left_pointer < right_pointer and
                       sorted_numbers[right_pointer] == sorted_numbers[right_pointer - 1]):
                    right_pointer -= 1

                # Move both pointers inward past the duplicates we just skipped
                left_pointer += 1
                right_pointer -= 1

            elif current_sum < 0:
                # Sum is too small; move left pointer right to increase it
                left_pointer += 1

            else:
                # Sum is too large; move right pointer left to decrease it
                right_pointer -= 1

    return found_triplets


def main() -> None:
    """
    Main function to demonstrate three_sum with examples.
    """
    numbers_one = [-1, 0, 1, 2, -1, -4]
    numbers_two = [0, 1, 1]
    numbers_three = [0, 0, 0]
    numbers_four = [-2, 0, 1, 1, 2]

    print("Input: " + str(numbers_one))
    print("Triplets: " + str(three_sum(numbers_one)))
    print("")
    print("Input: " + str(numbers_two))
    print("Triplets: " + str(three_sum(numbers_two)))
    print("")
    print("Input: " + str(numbers_three))
    print("Triplets: " + str(three_sum(numbers_three)))
    print("")
    print("Input: " + str(numbers_four))
    print("Triplets: " + str(three_sum(numbers_four)))


if __name__ == "__main__":
    main()
