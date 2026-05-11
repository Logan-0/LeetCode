def first_bad_version(n: int) -> int:
    """
    You are a product manager and currently leading a team to develop a new product.
    Unfortunately, the latest version of your product fails the quality check.
    Since each version is developed based on the previous version, all the versions
    after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first
    bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version
    is bad. Implement a function to find the first bad version. You should minimize
    the number of calls to the API.

    LeetCode #278 - First Bad Version
    Difficulty: Easy
    Pattern: Binary Search

    Example:
        Input:  n = 5, bad = 4
        Output: 4
        Explanation: Version 4 is the first bad version

    Hint: Use binary search. All versions before the first bad one are good,
          all versions after are bad. Find the boundary.

    Time complexity goal: O(log n)
    Space complexity goal: O(1)

    Args:
        n: The number of versions

    Returns:
        The first bad version
    """
    pass


def is_bad_version(version: int) -> bool:
    """
    Mock API for testing. In real LeetCode, this is provided.
    For testing, we'll assume the first bad version is configurable.
    """
    # This is a mock - in actual implementation, this would be provided by LeetCode
    # For testing purposes, we can set this to return True for versions >= some threshold
    global first_bad
    return version >= first_bad


def main() -> None:
    """
    Main function to demonstrate first_bad_version with examples.
    """
    global first_bad
    first_bad = 4
    result = first_bad_version(5)
    print("First bad version: " + str(result))


if __name__ == "__main__":
    main()
