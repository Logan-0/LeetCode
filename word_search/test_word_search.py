from word_search import exist


def test_word_search():
    print("Testing exist...")

    # Test case 1: board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED" -> True
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    result = exist(board, "ABCCED")
    expected = True
    print(f"exist(board, 'ABCCED') = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="SEE" -> True
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    result = exist(board, "SEE")
    expected = True
    print(f"exist(board, 'SEE') = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB" -> False
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    result = exist(board, "ABCB")
    expected = False
    print(f"exist(board, 'ABCB') = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: board=[["A"]], word="A" -> True
    board = [["A"]]
    result = exist(board, "A")
    expected = True
    print(f"exist([['A']], 'A') = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: board=[["A","A"]], word="AAA" -> False
    board = [["A","A"]]
    result = exist(board, "AAA")
    expected = False
    print(f"exist([['A','A']], 'AAA') = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_word_search()
