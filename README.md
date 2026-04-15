# LeetCode Solutions

A collection of Python solutions for various LeetCode problems, organized by topic and algorithmic approach.

## Overview

This repository contains my implementations of common LeetCode problems, focusing on understanding different algorithmic approaches and their trade-offs. Each problem often includes multiple solutions demonstrating different techniques (brute force vs optimized approaches).

## Structure

- **Problem Solutions**: Individual Python files for each LeetCode problem
- **Study Guide**: Comprehensive documentation (`LEETCODE_STUDY_GUIDE.md`) covering patterns, principles, and tips

## Covered Topics

- Array & Hash Table Problems
- Linked List Problems
- Stack & Queue Problems
- Tree Problems
- Backtracking & Recursion
- Heap & Priority Queue
- Sorting & Searching
- Greedy Algorithms
- Two Pointer Technique

## Key Features

- **Multiple Approaches**: Many problems include both brute force and optimized solutions
- **Detailed Documentation**: Each solution includes time/space complexity analysis
- **Pattern Recognition**: Focus on identifying common algorithmic patterns
- **Educational Focus**: Comments and explanations for learning purposes

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/[your-username]/LeetCode.git
   cd LeetCode
   ```

2. Review the study guide:
   ```bash
   cat LEETCODE_STUDY_GUIDE.md
   ```

3. Run individual solutions:
   ```bash
   python twoSumOnePassHash.py
   ```

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
