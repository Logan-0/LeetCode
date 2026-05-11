# LeetCode Learning Roadmap

**Last Updated**: May 11, 2026
**Total Problems**: 53
**Completed**: 35 | **Stub/New**: 18

---

## Incomplete Problems (HIGH PRIORITY)

### Problems Requiring Implementation

| Problem | Difficulty | Pattern | Status |
|---------|------------|---------|--------|
| [House Robber](house_robber/) | Medium | Dynamic Programming | ❌ Stub Only |
| [Jump Game](jump_game/) | Medium | Greedy | ❌ Stub Only |
| [Number of 1 Bits](number_of_1_bits/) | Easy | Bit Manipulation | 📝 Stub |
| [Single Number](single_number/) | Easy | Bit Manipulation | 📝 Stub |
| [Search Insert Position](search_insert_position/) | Easy | Binary Search | 📝 Stub |
| [First Bad Version](first_bad_version/) | Easy | Binary Search | 📝 Stub |
| [Symmetric Tree](symmetric_tree/) | Easy | Tree/DFS | 📝 Stub |
| [Same Tree](same_tree/) | Easy | Tree/DFS | 📝 Stub |
| [Invert Binary Tree](invert_binary_tree/) | Easy | Tree/DFS | 📝 Stub |
| [Plus One](plus_one/) | Easy | Array/Math | 📝 Stub |
| [Move Zeroes](move_zeroes/) | Easy | Two Pointers | 📝 Stub |
| [Course Schedule](course_schedule/) | Medium | Graph/BFS/DFS | 📝 Stub |
| [Clone Graph](clone_graph/) | Medium | Graph/BFS/DFS | 📝 Stub |
| [Word Search](word_search/) | Medium | DFS/Backtracking | 📝 Stub |
| [Subsets](subsets/) | Medium | Backtracking | 📝 Stub |
| [Permutations](permutations/) | Medium | Backtracking | 📝 Stub |
| [Sort Colors](sort_colors/) | Medium | Two Pointers | 📝 Stub |
| [Find Minimum in Rotated Sorted Array](find_minimum_rotated/) | Medium | Binary Search | 📝 Stub |

### Problems Needing Fixes

| Problem | Difficulty | Pattern | Status |
|---------|------------|---------|--------|
| [Container With Most Water](container_with_most_water/) | Medium | Two Pointers | ⚠️ Incorrect Implementation |

---

## Algorithmic Patterns

### 1. Hash Map Pattern
**When to Use**: O(1) lookup, counting elements, complement problems
**Time Complexity**: O(n) typical
**Space Complexity**: O(n)

**Examples**:
- Two Sum - Find complement pairs
- Contains Duplicate - Track seen elements
- Group Anagrams - Group by character signatures
- Top K Frequent Elements - Count frequencies
- Verifying Alien Dictionary - Custom ordering

### 2. Two Pointers Pattern
**When to Use**: Sorted arrays, sliding window, removing duplicates
**Time Complexity**: O(n) typical
**Space Complexity**: O(1)

**Examples**:
- Valid Palindrome - Compare from ends
- Merge Sorted Array - Merge in place backwards
- Merge Two Sorted Lists - Merge linked lists
- Container With Most Water - Shrink from widest
- Three Sum - Sort + two pointers

### 3. Stack Pattern
**When to Use**: Matching brackets, monotonic problems, "next greater element"
**Time Complexity**: O(n) typical
**Space Complexity**: O(n)

**Examples**:
- Valid Parentheses - Match opening/closing
- Min Stack - Track minimum with auxiliary stack
- Daily Temperatures - Find next warmer day
- Final Prices With Discount - Apply discounts

### 4. Heap / Priority Queue Pattern
**When to Use**: "Top K" problems, streaming minimums/maximums
**Time Complexity**: O(n log k) or O(log n) per operation
**Space Complexity**: O(k) or O(n)

**Examples**:
- Kth Largest Element in Stream - Maintain min-heap of size k
- Top K Frequent Elements - Can use heap optimization

### 5. Backtracking Pattern
**When to Use**: Generating all combinations or permutations
**Time Complexity**: Exponential (O(2^n), O(n!), O(k^n))
**Space Complexity**: O(n) recursion depth

**Examples**:
- Generate Parentheses - Build valid combinations
- Letter Combinations of a Phone Number - Cartesian product

### 6. Dynamic Programming Pattern
**When to Use**: Overlapping sub-problems, optimal sub-structure
**Time Complexity**: O(n × m) or O(n^2) typical
**Space Complexity**: O(n) or O(n × m)

**Examples**:
- Climbing Stairs - Fibonacci-like
- Coin Change - Minimum coins
- Longest Increasing Subsequence - Build optimal sequence
- Maximum Subarray - Kadane's algorithm
- House Robber - Can't rob adjacent houses

### 7. BFS / DFS Pattern
**When to Use**: Tree traversal, grid exploration, connected components
**Time Complexity**: O(V + E) or O(n)
**Space Complexity**: O(h) for DFS, O(w) for BFS

**Examples**:
- Number of Islands - Grid exploration
- Maximum Depth of Binary Tree - Tree recursion
- Count Complete Tree Nodes - Tree traversal
- Reverse Linked List - Iterative pointer manipulation

### 8. Greedy Pattern
**When to Use**: Local optimal leads to global optimal
**Time Complexity**: O(n) or O(n log n)
**Space Complexity**: O(1) or O(n)

**Examples**:
- Best Time to Buy and Sell Stock - Capture all profits
- Jump Game - Track furthest reachable
- Merge Intervals - Sort + greedy merge

### 9. Bit Manipulation Pattern
**When to Use**: Operations on binary representation, XOR tricks
**Time Complexity**: O(1) or O(n) depending on operations
**Space Complexity**: O(1)

**Examples**:
- Number of 1 Bits - Count set bits using n & (n-1)
- Single Number - XOR all elements to find unique

### 10. Graph Algorithms Pattern
**When to Use**: Cycle detection, traversal, topological sort
**Time Complexity**: O(V + E)
**Space Complexity**: O(V + E)

**Examples**:
- Course Schedule - Detect cycles in directed graph
- Clone Graph - Deep copy using BFS/DFS

### 11. Trie Pattern
**When to Use**: String matching, autocomplete
**Time Complexity**: O(m) for search, O(n*m) for construction
**Space Complexity**: O(n*m)

**Examples**:
- Implement Trie - Basic trie operations
- Word Search II - Use trie for efficient lookup

---

## Completed Problems by Difficulty

### Easy Problems (16 completed, 9 new stubs)

| Problem | Pattern | Time Complexity | Space Complexity | Status |
|---------|---------|-----------------|------------------|--------|
| Contains Duplicate | Hash Map | O(n) | O(n) | ✅ Complete |
| Valid Palindrome | Two Pointers | O(n) | O(1) | ✅ Complete |
| Binary Search | Binary Search | O(log n) | O(1) | ✅ Complete |
| Climbing Stairs | Dynamic Programming | O(n) | O(1) | ✅ Complete |
| Missing Number | Hash Map/Math | O(n) | O(1) | ✅ Complete |
| Maximum Subarray | Dynamic Programming | O(n) | O(1) | ✅ Complete |
| Maximum Depth of Binary Tree | DFS | O(n) | O(h) | ✅ Complete |
| Merge Sorted Array | Two Pointers | O(n + m) | O(1) | ✅ Complete |
| Final Prices With Discount | Stack | O(n) | O(n) | ✅ Complete |
| Best Time to Buy and Sell Stock | Greedy | O(n) | O(1) | ✅ Complete |
| Merge Two Sorted Lists | Two Pointers | O(n + m) | O(1) | ✅ Complete |
| Count Complete Tree Nodes | DFS | O(n) | O(h) | ✅ Complete |
| Two Sum (Brute Force) | Brute Force | O(n²) | O(1) | ✅ Complete |
| Two Sum (Hash Map) | Hash Map | O(n) | O(n) | ✅ Complete |
| Valid Parentheses | Stack | O(n) | O(n) | ✅ Complete |
| Reverse Linked List | Pointers | O(n) | O(1) | ✅ Complete |
| Number of 1 Bits | Bit Manipulation | O(1) | O(1) | 📝 Stub |
| Single Number | Bit Manipulation | O(n) | O(1) | 📝 Stub |
| Search Insert Position | Binary Search | O(log n) | O(1) | 📝 Stub |
| First Bad Version | Binary Search | O(log n) | O(1) | 📝 Stub |
| Symmetric Tree | Tree/DFS | O(n) | O(h) | 📝 Stub |
| Same Tree | Tree/DFS | O(min(m,n)) | O(h) | 📝 Stub |
| Invert Binary Tree | Tree/DFS | O(n) | O(h) | 📝 Stub |
| Plus One | Array/Math | O(n) | O(1) | 📝 Stub |
| Move Zeroes | Two Pointers | O(n) | O(1) | 📝 Stub |

### Medium Problems (18 completed, 7 new stubs)

| Problem | Pattern | Time Complexity | Space Complexity | Status |
|---------|---------|-----------------|------------------|--------|
| Longest Palindromic Substring | Two Pointers | O(n²) | O(1) | ✅ Complete |
| Add Two Numbers | Linked List | O(max(n,m)) | O(max(n,m)) | ✅ Complete |
| Coin Change | Dynamic Programming | O(n × m) | O(m) | ✅ Complete |
| Daily Temperatures | Stack | O(n) | O(n) | ✅ Complete |
| Min Stack | Auxiliary Stack | O(1) all ops | O(n) | ✅ Complete |
| Generate Parentheses | Backtracking | O(4^n/√n) | O(n) | ✅ Complete |
| Letter Combinations of a Phone Number | Backtracking | O(4^n) | O(4^n) | ✅ Complete |
| Closest Target in a Circular Array | Two Pointers | O(n) | O(1) | ✅ Complete |
| Kth Largest Element in a Stream | Heap | O(log k) per add | O(k) | ✅ Complete |
| Longest Consecutive Sequence | Sort + Scan | O(n log n) | O(n) | ✅ Complete |
| Longest Increasing Subsequence | Dynamic Programming | O(n²) | O(n) | ✅ Complete |
| Merge Intervals | Sort + Greedy | O(n log n) | O(n) | ✅ Complete |
| Longest Substring Without Repeating Characters | Sliding Window | O(n) | O(min(n,m)) | ✅ Complete |
| Verifying Alien Dictionary | Hash Map | O(n × m) | O(1) | ✅ Complete |
| Top K Frequent Elements | Frequency Count | O(n log n) | O(n) | ✅ Complete |
| Group Anagrams | Hash Map | O(n × k log k) | O(n × k) | ✅ Complete |
| Spiral Matrix | Simulation | O(n × m) | O(1) | ✅ Complete |
| Product Except Self | Two Pass | O(n) | O(1) | ✅ Complete |
| Course Schedule | Graph/BFS/DFS | O(V + E) | O(V + E) | 📝 Stub |
| Clone Graph | Graph/BFS/DFS | O(V + E) | O(V) | 📝 Stub |
| Word Search | DFS/Backtracking | O(N × 3^L) | O(L) | 📝 Stub |
| Subsets | Backtracking | O(N × 2^N) | O(N) | 📝 Stub |
| Permutations | Backtracking | O(N × N!) | O(N) | 📝 Stub |
| Sort Colors | Two Pointers | O(n) | O(1) | 📝 Stub |
| Find Minimum in Rotated Sorted Array | Binary Search | O(log n) | O(1) | 📝 Stub |

---

## Learning Path by Difficulty

### Phase 1: Foundation (Easy Problems)
**Focus**: Basic patterns, simple data structures

1. **Hash Map Basics**
   - Contains Duplicate
   - Two Sum (Hash Map version)

2. **Two Pointers Introduction**
   - Valid Palindrome
   - Merge Sorted Array
   - Move Zeroes (NEW)

3. **Stack Fundamentals**
   - Valid Parentheses

4. **Tree Traversal**
   - Maximum Depth of Binary Tree
   - Count Complete Tree Nodes
   - Symmetric Tree (NEW)
   - Same Tree (NEW)
   - Invert Binary Tree (NEW)

5. **Dynamic Programming Basics**
   - Climbing Stairs
   - Maximum Subarray

6. **Linked Lists**
   - Merge Two Sorted Lists
   - Reverse Linked List

7. **Binary Search**
   - Binary Search
   - Search Insert Position (NEW)
   - First Bad Version (NEW)

8. **Bit Manipulation (NEW)**
   - Number of 1 Bits (NEW)
   - Single Number (NEW)

9. **Array/Math**
   - Missing Number
   - Plus One (NEW)

### Phase 2: Intermediate (Medium Problems)
**Focus**: Complex patterns, optimization

1. **Advanced Hash Map**
   - Group Anagrams
   - Verifying Alien Dictionary
   - Top K Frequent Elements

2. **Advanced Two Pointers**
   - Longest Palindromic Substring
   - Three Sum
   - Longest Substring Without Repeating Characters
   - Sort Colors (NEW)

3. **Stack Applications**
   - Min Stack
   - Daily Temperatures
   - Final Prices With Discount

4. **Dynamic Programming**
   - Coin Change
   - Longest Increasing Subsequence
   - House Robber (TODO)

5. **Backtracking**
   - Generate Parentheses
   - Letter Combinations of a Phone Number
   - Subsets (NEW)
   - Permutations (NEW)

6. **Heap/Priority Queue**
   - Kth Largest Element in a Stream

7. **Greedy Algorithms**
   - Best Time to Buy and Sell Stock
   - Merge Intervals
   - Jump Game (TODO)

8. **BFS/DFS**
   - Number of Islands
   - Word Search (NEW)

9. **Graph Algorithms (NEW)**
   - Course Schedule (NEW)
   - Clone Graph (NEW)

10. **Matrix Problems**
    - Spiral Matrix
    - Search 2D Matrix
    - Rotate Image
    - Container With Most Water (needs fix)

11. **Linked Lists Advanced**
    - Add Two Numbers

12. **Array Manipulation**
    - Product Except Self
    - Longest Consecutive Sequence
    - Closest Target in a Circular Array

13. **Binary Search**
    - Find Minimum in Rotated Sorted Array (NEW)

---

## Complexity Reference

| Complexity | Description | Typical Operations |
|------------|-------------|-------------------|
| O(1) | Constant | Hash map lookup, array access |
| O(log n) | Logarithmic | Binary search, heap operations |
| O(n) | Linear | Single loop, hash map iteration |
| O(n log n) | Linearithmic | Sorting, heap operations |
| O(n²) | Quadratic | Nested loops, some DP |
| O(2^n) | Exponential | Backtracking, brute force |
| O(n!) | Factorial | Permutations |

---

## Next Steps

### Immediate (Incomplete Problems)
1. ✅ **Fix Container With Most Water** - Implement proper two-pointer solution
2. ✅ **Implement House Robber** - Dynamic programming solution
3. ✅ **Implement Jump Game** - Greedy algorithm

### New Stub Problems (18 total)
**Easy (9 new):**
- Number of 1 Bits - Bit Manipulation
- Single Number - Bit Manipulation
- Search Insert Position - Binary Search
- First Bad Version - Binary Search
- Symmetric Tree - Tree/DFS
- Same Tree - Tree/DFS
- Invert Binary Tree - Tree/DFS
- Plus One - Array/Math
- Move Zeroes - Two Pointers

**Intermediate (7 new):**
- Course Schedule - Graph/BFS/DFS
- Clone Graph - Graph/BFS/DFS
- Word Search - DFS/Backtracking
- Subsets - Backtracking
- Permutations - Backtracking
- Sort Colors - Two Pointers
- Find Minimum in Rotated Sorted Array - Binary Search

### Future Additions
Consider adding these patterns and problems:
- Graph algorithms (Dijkstra, BFS/DFS on graphs)
- Trie data structure
- Segment Tree
- Binary Indexed Tree
- More advanced DP problems
- Hard difficulty problems
