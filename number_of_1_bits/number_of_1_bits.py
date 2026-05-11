def hamming_weight(n: int) -> int:
    """
    Write a function that takes the binary representation of an unsigned integer
    and returns the number of '1' bits it has (also known as the Hamming weight).

    LeetCode #191 - Number of 1 Bits
    Difficulty: Easy
    Pattern: Bit Manipulation

    Example:
        Input:  n = 11 (binary: 00000000000000000000000000001011)
        Output: 3

        Input:  n = 128 (binary: 00000000000000000000000010000000)
        Output: 1

    Hint: Use bit manipulation tricks. The operation n & (n - 1) clears the
          least significant '1' bit. Count how many times you can do this
          before n becomes 0.

    Time complexity goal: O(1) - at most 32 iterations for 32-bit integer
    Space complexity goal: O(1)

    Args:
        n: An unsigned integer

    Returns:
        The number of '1' bits in the binary representation of n
    """
    pass


def main() -> None:
    """
    Main function to demonstrate hamming_weight with examples.
    """
    result = hamming_weight(11)
    print("Hamming weight of 11: " + str(result))


if __name__ == "__main__":
    main()
