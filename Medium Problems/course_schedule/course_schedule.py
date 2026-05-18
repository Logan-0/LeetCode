def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    There are a total of num_courses courses you have to take, labeled from 0 to
    num_courses - 1. You are given an array prerequisites where prerequisites[i] =
    [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1] indicates that to take course 0 you have to first
    take course 1. Return true if you can finish all courses. Otherwise, return false.

    LeetCode #207 - Course Schedule
    Difficulty: Medium
    Pattern: Graph / BFS / DFS

    Example:
        Input:  num_courses = 2, prerequisites = [[1,0]]
        Output: True

        Input:  num_courses = 2, prerequisites = [[1,0],[0,1]]
        Output: False

    Hint: This is a cycle detection problem in a directed graph. Build the graph
          from prerequisites and detect if there's a cycle using DFS or BFS (Kahn's algorithm).

    Time complexity goal: O(V + E) - V = courses, E = prerequisites
    Space complexity goal: O(V + E)

    Args:
        num_courses: The total number of courses
        prerequisites: List of prerequisite pairs [course, prerequisite]

    Returns:
        True if all courses can be finished, False otherwise

    Time Complexity: O(V + E) -- where V is courses, E is prerequisites
    Space Complexity: O(V + E) -- storing graph and visited state
    """
    pass


def main() -> None:
    """
    Main function to demonstrate can_finish with examples.
    """
    result = can_finish(2, [[1, 0]])
    print("Can finish courses: " + str(result))


if __name__ == "__main__":
    main()
