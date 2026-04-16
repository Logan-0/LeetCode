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
