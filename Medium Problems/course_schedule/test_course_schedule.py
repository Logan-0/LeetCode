from course_schedule import can_finish


def test_course_schedule():
    print("Testing can_finish...")

    # Test case 1: num_courses=2, prerequisites=[[1,0]] -> True
    result = can_finish(2, [[1, 0]])
    expected = True
    print(f"can_finish(2, [[1,0]]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: num_courses=2, prerequisites=[[1,0],[0,1]] -> False
    result = can_finish(2, [[1, 0], [0, 1]])
    expected = False
    print(f"can_finish(2, [[1,0],[0,1]]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: num_courses=1, prerequisites=[] -> True
    result = can_finish(1, [])
    expected = True
    print(f"can_finish(1, []) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: num_courses=5, prerequisites=[[0,1],[0,2],[1,3],[1,4]] -> True
    result = can_finish(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
    expected = True
    print(f"can_finish(5, [[0,1],[0,2],[1,3],[1,4]]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: num_courses=3, prerequisites=[[0,1],[1,2],[2,0]] -> False
    result = can_finish(3, [[0, 1], [1, 2], [2, 0]])
    expected = False
    print(f"can_finish(3, [[0,1],[1,2],[2,0]]) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_course_schedule()
