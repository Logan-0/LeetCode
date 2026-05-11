from number_of_1_bits import hamming_weight


def test_number_of_1_bits():
    print("Testing hamming_weight...")

    # Test case 1: 11 (binary: 1011) has 3 ones
    result = hamming_weight(11)
    expected = 3
    print(f"hamming_weight(11) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 2: 128 (binary: 10000000) has 1 one
    result = hamming_weight(128)
    expected = 1
    print(f"hamming_weight(128) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 3: 0 has 0 ones
    result = hamming_weight(0)
    expected = 0
    print(f"hamming_weight(0) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 4: 7 (binary: 111) has 3 ones
    result = hamming_weight(7)
    expected = 3
    print(f"hamming_weight(7) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    # Test case 5: 255 (binary: 11111111) has 8 ones
    result = hamming_weight(255)
    expected = 8
    print(f"hamming_weight(255) = {result}, expected {expected}")
    assert result == expected, f"FAIL: Expected {expected}, got {result}"

    print("PASS: All test cases passed!")


if __name__ == "__main__":
    test_number_of_1_bits()
