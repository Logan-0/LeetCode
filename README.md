# LeetCode Solutions

A collection of Python solutions for common LeetCode problems. Each problem is solved
with care for readability, and many are solved **twice** — once the slow, obvious way
and once the fast, clever way — so you can see exactly what the improvement buys you.

---

## What is an Algorithm?

An **algorithm** is a step-by-step set of instructions for solving a problem. A recipe
is an algorithm. The directions on a GPS are an algorithm. In programming, we write
algorithms that tell the computer exactly how to process data.

Two algorithms can solve the same problem but take wildly different amounts of time
or memory. Part of being a good programmer is knowing which algorithm to reach for
and why.

## Structure

- **Problem Solutions**: Individual Python files, one per problem
- **Documentation**: See the `docs/` folder for detailed documentation:
  - `docs/HowItWorks.md` — Comprehensive guide to algorithmic patterns and problem-solving strategies
  - `docs/RoadMap.md` — Project status and future work
  - `docs/ProjectSummary.md` — Feature summary
  - `docs/ChangeLog.md` — Version history

---

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/[your-username]/LeetCode.git
   cd LeetCode
   ```

2. Read the documentation:
   ```bash
   cat docs/HowItWorks.md
   ```

3. Run any solution directly:
   ```bash
   python twoSumOnePassHash.py
   ```

## Practice Problems

These problems have test suites ready but **solution files are intentionally left blank** —
your job is to implement the function until all tests pass. Each directory contains:

- `<name>.py` — the solution stub with a full docstring explaining the problem. Write your code here.
- `test_<name>.py` — ready-made test cases. Run from inside the directory with `python test_<name>.py`.

When all tests print `PASS`, your solution is correct.

### Easy

| Problem | Topic | LeetCode # | Status | Solution File | Test File |
|---------|-------|------------|--------|---------------|-----------|
| Contains Duplicate | Array / Hash Set | #217 | Done | [contains_duplicate.py](contains_duplicate/contains_duplicate.py) | [test_contains_duplicate.py](contains_duplicate/test_contains_duplicate.py) |
| Maximum Subarray | Array / DP (Kadane's) | #53 | Done | [maximum_subarray.py](maximum_subarray/maximum_subarray.py) | [test_maximum_subarray.py](maximum_subarray/test_maximum_subarray.py) |
| Valid Palindrome | String / Two Pointers | #125 | Done | [valid_palindrome.py](valid_palindrome/valid_palindrome.py) | [test_valid_palindrome.py](valid_palindrome/test_valid_palindrome.py) |
| Missing Number | Array / Math | #268 | Done | [missing_number.py](missing_number/missing_number.py) | [test_missing_number.py](missing_number/test_missing_number.py) |
| Maximum Depth of Binary Tree | Tree / DFS | #104 | Done | [maximum_depth_binary_tree.py](maximum_depth_binary_tree/maximum_depth_binary_tree.py) | [test_maximum_depth_binary_tree.py](maximum_depth_binary_tree/test_maximum_depth_binary_tree.py) |
| Two Sum (Brute Force) | Array / Brute Force | #1 | Done | [twoSumBruteForce.py](two_sum/twoSumBruteForce.py) | N/A |
| Two Sum (Hash Map) | Array / Hash Map | #1 | Done | [twoSumOnePassHash.py](two_sum/twoSumOnePassHash.py) | N/A |
| Merge Sorted Array | Array / Two Pointers | #88 | Done | [mergeSortedArray.py](merge_sorted_array/mergeSortedArray.py) | [test_merge_sorted_array.py](merge_sorted_array/test_merge_sorted_array.py) |
| Final Prices With a Discount | Array / Stack | #1475 | Done | [finalPricesWithDiscount.py](final_prices_with_discount/finalPricesWithDiscount.py) | N/A |
| Best Time to Buy and Sell Stock | Array / Greedy | #121 | Done | [maxProfitStocks.py](max_profit_stocks/maxProfitStocks.py) | N/A |
| Merge Two Sorted Lists | Linked List / Two Pointers | #21 | Done | [mergeTwoSortedLinkedLists.py](merge_two_sorted_lists/mergeTwoSortedLinkedLists.py) | N/A |
| Count Complete Tree Nodes | Tree / Binary Search | #222 | Done | [countCompleteTreeNodes.py](count_complete_tree_nodes/countCompleteTreeNodes.py) | N/A |
| Binary Search | Array / Binary Search | #704 | Done | [binary_search.py](binary_search/binary_search.py) | [test_binary_search.py](binary_search/test_binary_search.py) |
| Climbing Stairs | DP / Fibonacci | #70 | Done | [climbing_stairs.py](climbing_stairs/climbing_stairs.py) | [test_climbing_stairs.py](climbing_stairs/test_climbing_stairs.py) |

### Medium

| Problem | Topic | LeetCode # | Status | Solution File | Test File |
|---------|-------|------------|--------|---------------|-----------|
| Longest Palindromic Substring | String / Expand Around Center | #5 | Done | [longest_palindromic_substring.py](longest_palindromic_substring/longest_palindromic_substring.py) | [test_longest_palindromic_substring.py](longest_palindromic_substring/test_longest_palindromic_substring.py) |
| Add Two Numbers | Linked List / Math | #2 | Done | [addTwoNumbers.py](add_two_numbers/addTwoNumbers.py) | N/A |
| Coin Change | DP / Memoization | #322 | Done | [coinChangeDp.py](coin_change/coinChangeDp.py) | N/A |
| Daily Temperatures | Array / Hash Map | #739 | Done | [dailyTemperatures.py](daily_temperatures/dailyTemperatures.py) | N/A |
| Min Stack | Stack / Design | #155 | Done | [minStack.py](min_stack/minStack.py) | N/A |
| Generate Parentheses | Backtracking | #22 | Done | [generateParenthesis.py](generate_parenthesis/generateParenthesis.py) | N/A |
| Letter Combinations of a Phone Number | Backtracking | #17 | Done | [letterCombinationsOfAPhoneNumber.py](letter_combinations_phone_number/letterCombinationsOfAPhoneNumber.py) | N/A |
| Closest Target in a Circular Array | Array / Circular | #? | Done | [closestTargerCircleArray.py](closest_target_circle_array/closestTargerCircleArray.py) | N/A |
| Kth Largest Element in a Stream | Heap / Priority Queue | #703 | Done | [kthLargestElement.py](kth_largest_element/kthLargestElement.py) | N/A |
| Longest Consecutive Sequence | Array / Hash Set | #128 | Done | [longestConseqSeq.py](longest_consecutive_sequence/longestConseqSeq.py) | N/A |
| Longest Increasing Subsequence | DP | #300 | Done | [longestIncSubseq.py](longest_increasing_subsequence/longestIncSubseq.py) | N/A |
| Merge Intervals | Array / Sorting | #56 | Done | [mergeIntervals.py](merge_intervals/mergeIntervals.py) | N/A |
| Longest Substring Without Repeating Characters | String / Sliding Window | #3 | Done | [lengthOfLongestSubstring.py](longest_substring/lengthOfLongestSubstring.py) | N/A |
| Verifying an Alien Dictionary | String / Hash Map | #953 | Done | [verifyingAlienDictionary.py](verifying_alien_dictionary/verifyingAlienDictionary.py) | N/A |
| Top K Frequent Elements | Array / Hash Map | #347 | Done | [topKfreqElems.py](top_k_frequent_elements/topKfreqElems.py) | N/A |
| Group Anagrams | Hash Map / Sorting | #49 | Done | [group_anagrams.py](group_anagrams/group_anagrams.py) | [test_group_anagrams.py](group_anagrams/test_group_anagrams.py) |
| Spiral Matrix | Matrix / Simulation | #54 | Done | [spiral_matrix.py](spiral_matrix/spiral_matrix.py) | [test_spiral_matrix.py](spiral_matrix/test_spiral_matrix.py) |

### ToDo (Not Started)

| Problem | Topic | LeetCode # | Solution File | Test File |
|---------|-------|------------|---------------|-----------|
| House Robber | Dynamic Programming | #198 | [house_robber.py](house_robber/house_robber.py) | [test_house_robber.py](house_robber/test_house_robber.py) |
| Jump Game | Greedy | #55 | [jump_game.py](jump_game/jump_game.py) | [test_jump_game.py](jump_game/test_jump_game.py) |
| Container With Most Water | Two Pointers | #11 | [container_with_most_water.py](container_with_most_water/container_with_most_water.py) | [test_container_with_most_water.py](container_with_most_water/test_container_with_most_water.py) |

---

## Problem List

### Array & Hashing
- `twoSumBruteForce.py` - Two Sum (Brute Force)
- `twoSumOnePassHash.py` - Two Sum (Hash Map)
- `mergeSortedArray.py` - Merge Sorted Array
- `topKfreqElems.py` - Top K Frequent Elements
- `finalPricesWithDiscount.py` - Final Prices With a Discount
- `maxProfitStocks.py` - Best Time to Buy and Sell Stock
- `closestTargerCircleArray.py` - Closest Target in a Circular Array
- `verifyingAlienDictionary.py` - Verifying an Alien Dictionary

### Linked Lists
- `mergeTwoSortedLinkedLists.py` - Merge Two Sorted Lists
- `addTwoNumbers.py` - Add Two Numbers

### Trees
- `countCompleteTreeNodes.py` - Count Complete Tree Nodes
- `numberOfIslands.py` - Number of Islands (DFS)

### Dynamic Programming
- `coinChangeDp.py` - Coin Change (Dynamic Programming)
- `coinChangeGreedy.py` - Coin Change (Greedy)
- `longestIncSubseq.py` - Longest Increasing Subsequence
- `longestConseqSeq.py` - Longest Consecutive Sequence

### Stack & Queue
- `dailyTemperatures.py` - Daily Temperatures (Forward Iteration)
- `dailyTemperaturesStack.py` - Daily Temperatures (Monotonic Stack)
- `minStack.py` - Min Stack

### Two Pointer Technique
- `lengthOfLongestSubstring.py` - Longest Substring Without Repeating Characters (Brute Force)
- `lengthOfLongestSubstringSlidingWindow.py` - Longest Substring Without Repeating Characters (Sliding Window)

### Heap & Priority Queue
- `kthLargestElement.py` - Kth Largest Element in a Stream

### Backtracking & Recursion
- `generateParenthesis.py` - Generate Parentheses
- `letterCombinationsOfAPhoneNumber.py` - Letter Combinations of a Phone Number

### Sorting & Searching
- `mergeIntervals.py` - Merge Intervals
- `search2DMatrix.py` - Search a 2D Matrix

## Code Style Guidelines

All solutions in this repository follow these coding style guidelines:

### Comment and Code Spacing

- **Comment followed by code**: No empty line needed between comment and code
  ```
  # This is a comment
  some_code_here
  ```

- **Code followed by comment**: Empty line required between code and comment
  ```
  some_code_here
  
  # This is a comment
  ```

- **Indented blocks**:
  - If there's only a single line of code under indentation, no blank line needed
  - If there are multiple lines of code under indentation, blank line required to separate the block

### Print Statements

- Use standard print statements with string concatenation or formatting instead of f-strings
  ```
  print("Result: " + str(result))
  ```
  NOT:
  ```
  print(f"Result: {result}")
  ```

### Variable Naming

- Use descriptive variable names (no single-letter variables)
- Variable names should clearly indicate their purpose
- Example: `current_index` instead of `i`, `target_value` instead of `t`

### Function Style

- Use functional programming style (standalone functions) instead of class-based solutions
- No class instantiation required to use the solutions
- Stateful classes converted to closure-based factories where appropriate

### Documentation

- All functions include detailed docstrings explaining the algorithm
- Inline comments explain each step for educational purposes
- Time and space complexity documented where relevant

## Contributing

This is a personal learning repository. Feel free to fork and use it for your own LeetCode practice!

## License

This project is open source and available under the [MIT License](LICENSE).
