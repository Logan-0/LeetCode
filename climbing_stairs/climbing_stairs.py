def climb_stairs(step_count: int) -> int:
    """
    Counts the number of distinct ways to climb to the top of a staircase,
    where each move can advance either 1 or 2 steps.

    The key insight: to reach step n, you must have come from step n-1
    (by taking 1 step) or from step n-2 (by taking 2 steps). So the
    number of ways to reach step n equals the number of ways to reach
    step n-1 PLUS the number of ways to reach step n-2. This is the
    Fibonacci sequence in disguise!

    Base cases:
    - 1 step: exactly 1 way (take one single step)
    - 2 steps: exactly 2 ways (1+1 or just 2)

    Because we only ever look back two values, we can use two variables
    instead of an entire array, keeping space usage constant.

    Args:
        step_count: The total number of steps in the staircase (positive integer)

    Returns:
        The number of distinct ways to reach the top

    Time Complexity: O(n) -- one pass through from step 2 to step n
    Space Complexity: O(1) -- only two variables needed, not an array
    """

    # The one-step case cannot enter the loop, handle it separately
    if step_count == 1:
        return 1

    # Seed the first two Fibonacci-like values
    # ways_for_previous represents how many ways to reach the step just before current
    # ways_for_two_back represents how many ways to reach the step two before current
    ways_for_previous = 1
    ways_for_two_back = 1

    for current_step in range(2, step_count + 1):
        # Ways to reach this step = ways from one step back + ways from two steps back
        ways_for_current = ways_for_previous + ways_for_two_back

        # Slide the window forward before the next iteration
        ways_for_two_back = ways_for_previous
        ways_for_previous = ways_for_current

    return ways_for_previous


def main() -> None:
    """
    Main function to demonstrate climb_stairs with several staircase sizes.
    """
    print("Ways to climb 1 step:   " + str(climb_stairs(1)))
    print("Ways to climb 2 steps:  " + str(climb_stairs(2)))
    print("Ways to climb 3 steps:  " + str(climb_stairs(3)))
    print("Ways to climb 5 steps:  " + str(climb_stairs(5)))
    print("Ways to climb 10 steps: " + str(climb_stairs(10)))


if __name__ == "__main__":
    main()
