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

## What is Big O Notation?

Big O notation describes how the time (or memory) an algorithm uses **grows** as the
input size grows. The letter "n" stands for the size of the input.

| Notation | Plain English | Example |
|----------|--------------|---------|
| O(1) | Always the same speed, no matter how big the input | Reading one element from a list by index |
| O(log n) | Gets a tiny bit slower as input doubles | Binary search on a sorted list |
| O(n) | Proportionally slower as input grows | A single loop through a list |
| O(n log n) | Slightly worse than linear | Most efficient sorting algorithms |
| O(n²) | Much slower as input grows | A loop inside a loop |

A hash map lookup is O(1). A single loop is O(n). A loop inside a loop is O(n²).
Trading an O(n²) brute force for an O(n) hash map solution is a common pattern here.

## How to Approach a New Problem

1. **Read carefully.** What is the input? What is the expected output? Are there
   constraints (e.g., the list is always sorted)?
2. **Write a brute force solution first.** Even a slow, obvious answer proves you
   understand the problem.
3. **Find the bottleneck.** Where is the algorithm doing redundant work?
4. **Look for a pattern.** Most LeetCode problems fall into one of a handful of
   recurring patterns (see below).
5. **Optimize.** Replace the bottleneck with a faster data structure or technique.
6. **Analyze.** What is the time complexity? The space complexity?

## Recurring Patterns in This Repository

| Pattern | When to Use |
|---------|------------|
| **Hash Map** | Need O(1) lookup; counting elements; complement problems |
| **Two Pointers** | Sorted arrays; sliding window; removing duplicates |
| **Stack** | Matching brackets; monotonic problems; "next greater element" |
| **Heap / Priority Queue** | "Top K" problems; streaming minimums or maximums |
| **Backtracking** | Generating all combinations or permutations |
| **Dynamic Programming** | Overlapping sub-problems; optimal sub-structure |
| **BFS / DFS** | Tree traversal; grid exploration; connected components |

Recognizing which pattern fits a problem is the most valuable skill this repository
is designed to build.

---

## Structure

- **Problem Solutions**: Individual Python files, one per problem
- **Study Guide**: `LEETCODE_STUDY_GUIDE.md` — deep dives into every pattern with
  tips, common mistakes, and complexity analysis

---

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/[your-username]/LeetCode.git
   cd LeetCode
   ```

2. Read the study guide first:
   ```bash
   cat LEETCODE_STUDY_GUIDE.md
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

| Problem | Topic | LeetCode # | Solution File | Test File |
|---------|-------|------------|---------------|-----------|
| Contains Duplicate | Array / Hash Set | #217 | [contains_duplicate.py](contains_duplicate/contains_duplicate.py) | [test_contains_duplicate.py](contains_duplicate/test_contains_duplicate.py) |
| Maximum Subarray | Array / DP (Kadane's) | #53 | [maximum_subarray.py](maximum_subarray/maximum_subarray.py) | [test_maximum_subarray.py](maximum_subarray/test_maximum_subarray.py) |
| Valid Palindrome | String / Two Pointers | #125 | [valid_palindrome.py](valid_palindrome/valid_palindrome.py) | [test_valid_palindrome.py](valid_palindrome/test_valid_palindrome.py) |
| Missing Number | Array / Math | #268 | [missing_number.py](missing_number/missing_number.py) | [test_missing_number.py](missing_number/test_missing_number.py) |
| Maximum Depth of Binary Tree | Tree / DFS | #104 | [maximum_depth_binary_tree.py](maximum_depth_binary_tree/maximum_depth_binary_tree.py) | [test_maximum_depth_binary_tree.py](maximum_depth_binary_tree/test_maximum_depth_binary_tree.py) |

### Medium

| Problem | Topic | LeetCode # | Solution File | Test File |
|---------|-------|------------|---------------|-----------|
| House Robber | Dynamic Programming | #198 | [house_robber.py](house_robber/house_robber.py) | [test_house_robber.py](house_robber/test_house_robber.py) |
| Jump Game | Greedy | #55 | [jump_game.py](jump_game/jump_game.py) | [test_jump_game.py](jump_game/test_jump_game.py) |
| Container With Most Water | Two Pointers | #11 | [container_with_most_water.py](container_with_most_water/container_with_most_water.py) | [test_container_with_most_water.py](container_with_most_water/test_container_with_most_water.py) |
| Group Anagrams | Hash Map | #49 | [group_anagrams.py](group_anagrams/group_anagrams.py) | [test_group_anagrams.py](group_anagrams/test_group_anagrams.py) |
| Spiral Matrix | Matrix / Simulation | #54 | [spiral_matrix.py](spiral_matrix/spiral_matrix.py) | [test_spiral_matrix.py](spiral_matrix/test_spiral_matrix.py) |

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
