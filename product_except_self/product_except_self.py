def product_except_self(numbers: list[int]) -> list[int]:
    """
    Returns a new list where result[i] is the product of every element
    in numbers except numbers[i].

    Constraints that make this interesting:
    - Cannot use division (so we cannot just compute total product then divide)
    - Must run in O(n) time

    The trick is two passes:

    Forward pass (left products):
        result[i] = product of all elements to the LEFT of index i.
        Nothing is to the left of index 0, so result[0] = 1.

    Backward pass (right products):
        We maintain a running product of everything to the RIGHT of index i.
        We multiply result[i] by this running right product.
        Nothing is to the right of the last index, so we start with 1.

    Example with [1, 2, 3, 4]:
        After forward pass:  result = [1, 1, 2, 6]
          (result[0]=1, result[1]=1, result[2]=1*2=2, result[3]=1*2*3=6)
        Backward pass running_right starts at 1:
          i=3: result[3] = 6 * 1 = 6,  running_right = 1*4 = 4
          i=2: result[2] = 2 * 4 = 8,  running_right = 4*3 = 12
          i=1: result[1] = 1 * 12 = 12, running_right = 12*2 = 24
          i=0: result[0] = 1 * 24 = 24, running_right = 24*1 = 24
        Final: [24, 12, 8, 6]  -- which is correct.

    Args:
        numbers: A list of integers

    Returns:
        A list where result[i] is the product of all numbers except numbers[i]

    Time Complexity: O(n) -- two linear passes
    Space Complexity: O(1) extra -- the output array is not counted as extra space
    """

    number_count = len(numbers)

    # Initialize the result array; each element starts at 1
    result = [1] * number_count

    # Forward pass: fill result[i] with the product of everything to the LEFT of i
    running_left_product = 1
    for current_index in range(number_count):
        result[current_index] = running_left_product
        running_left_product = running_left_product * numbers[current_index]

    # Backward pass: multiply result[i] by the product of everything to the RIGHT of i
    running_right_product = 1
    for current_index in range(number_count - 1, -1, -1):
        result[current_index] = result[current_index] * running_right_product
        running_right_product = running_right_product * numbers[current_index]

    return result


def main() -> None:
    """
    Main function to demonstrate product_except_self with examples.
    """
    numbers_one = [1, 2, 3, 4]
    numbers_two = [-1, 1, 0, -3, 3]

    print("Input:  " + str(numbers_one))
    print("Output: " + str(product_except_self(numbers_one)))
    print("")
    print("Input:  " + str(numbers_two))
    print("Output: " + str(product_except_self(numbers_two)))


if __name__ == "__main__":
    main()
