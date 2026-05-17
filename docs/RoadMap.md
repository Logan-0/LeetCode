# LeetCode Learning Roadmap

**Last Updated**: May 11, 2026
**Total Problems**: 53
**Completed**: 35 | **Stub/New**: 18

---

## Incomplete Problems (HIGH PRIORITY)

### Problems Requiring Implementation

| Problem | Difficulty | Pattern | Status |
|---------|------------|---------|--------|
| [House Robber](Medium Problems/house_robber/) | Medium | Dynamic Programming | ❌ Stub Only |
| [Jump Game](Medium Problems/jump_game/) | Medium | Greedy | ❌ Stub Only |
| [Number of 1 Bits](Easy Problems/number_of_1_bits/) | Easy | Bit Manipulation | 📝 Stub |
| [Single Number](Easy Problems/single_number/) | Easy | Bit Manipulation | 📝 Stub |
| [Search Insert Position](Easy Problems/search_insert_position/) | Easy | Binary Search | 📝 Stub |
| [First Bad Version](Easy Problems/first_bad_version/) | Easy | Binary Search | 📝 Stub |
| [Symmetric Tree](Easy Problems/symmetric_tree/) | Easy | Tree/DFS | 📝 Stub |
| [Same Tree](Easy Problems/same_tree/) | Easy | Tree/DFS | 📝 Stub |
| [Invert Binary Tree](Easy Problems/invert_binary_tree/) | Easy | Tree/DFS | 📝 Stub |
| [Plus One](Easy Problems/plus_one/) | Easy | Array/Math | 📝 Stub |
| [Move Zeroes](Easy Problems/move_zeroes/) | Easy | Two Pointers | 📝 Stub |
| [Course Schedule](Medium Problems/course_schedule/) | Medium | Graph/BFS/DFS | 📝 Stub |
| [Clone Graph](Medium Problems/clone_graph/) | Medium | Graph/BFS/DFS | 📝 Stub |
| [Word Search](Medium Problems/word_search/) | Medium | DFS/Backtracking | 📝 Stub |
| [Subsets](Medium Problems/subsets/) | Medium | Backtracking | 📝 Stub |
| [Permutations](Medium Problems/permutations/) | Medium | Backtracking | 📝 Stub |
| [Sort Colors](Medium Problems/sort_colors/) | Medium | Two Pointers | 📝 Stub |
| [Find Minimum in Rotated Sorted Array](Medium Problems/find_minimum_rotated/) | Medium | Binary Search | 📝 Stub |

### Problems Needing Fixes

| Problem | Difficulty | Pattern | Status |
|---------|------------|---------|--------|
| [Container With Most Water](Medium Problems/container_with_most_water/) | Medium | Two Pointers | ⚠️ Incorrect Implementation |

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

**Note**: All problem directories are now organized by difficulty:
- Easy problems are in `Easy Problems/` directory
- Medium problems are in `Medium Problems/` directory

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
| [Contains Duplicate](Easy Problems/contains_duplicate/) | Hash Map | O(n) | O(n) | ✅ Complete |
| [Valid Palindrome](Easy Problems/valid_palindrome/) | Two Pointers | O(n) | O(1) | ✅ Complete |
| [Binary Search](Easy Problems/binary_search/) | Binary Search | O(log n) | O(1) | ✅ Complete |
| [Climbing Stairs](Easy Problems/climbing_stairs/) | Dynamic Programming | O(n) | O(1) | ✅ Complete |
| [Missing Number](Easy Problems/missing_number/) | Hash Map/Math | O(n) | O(1) | ✅ Complete |
| [Maximum Subarray](Easy Problems/maximum_subarray/) | Dynamic Programming | O(n) | O(1) | ✅ Complete |
| [Maximum Depth of Binary Tree](Easy Problems/maximum_depth_binary_tree/) | DFS | O(n) | O(h) | ✅ Complete |
| [Merge Sorted Array](Easy Problems/merge_sorted_array/) | Two Pointers | O(n + m) | O(1) | ✅ Complete |
| [Final Prices With Discount](Easy Problems/final_prices_with_discount/) | Stack | O(n) | O(n) | ✅ Complete |
| [Best Time to Buy and Sell Stock](Easy Problems/max_profit_stocks/) | Greedy | O(n) | O(1) | ✅ Complete |
| [Merge Two Sorted Lists](Easy Problems/merge_two_sorted_lists/) | Two Pointers | O(n + m) | O(1) | ✅ Complete |
| [Count Complete Tree Nodes](Easy Problems/count_complete_tree_nodes/) | DFS | O(n) | O(h) | ✅ Complete |
| [Two Sum (Brute Force)](Easy Problems/two_sum/) | Brute Force | O(n²) | O(1) | ✅ Complete |
| [Two Sum (Hash Map)](Easy Problems/two_sum/) | Hash Map | O(n) | O(n) | ✅ Complete |
| [Valid Parentheses](Easy Problems/valid_parentheses/) | Stack | O(n) | O(n) | ✅ Complete |
| [Reverse Linked List](Easy Problems/reverse_linked_list/) | Pointers | O(n) | O(1) | ✅ Complete |
| [Number of 1 Bits](Easy Problems/number_of_1_bits/) | Bit Manipulation | O(1) | O(1) | 📝 Stub |
| [Single Number](Easy Problems/single_number/) | Bit Manipulation | O(n) | O(1) | 📝 Stub |
| [Search Insert Position](Easy Problems/search_insert_position/) | Binary Search | O(log n) | O(1) | 📝 Stub |
| [First Bad Version](Easy Problems/first_bad_version/) | Binary Search | O(log n) | O(1) | 📝 Stub |
| [Symmetric Tree](Easy Problems/symmetric_tree/) | Tree/DFS | O(n) | O(h) | 📝 Stub |
| [Same Tree](Easy Problems/same_tree/) | Tree/DFS | O(min(m,n)) | O(h) | 📝 Stub |
| [Invert Binary Tree](Easy Problems/invert_binary_tree/) | Tree/DFS | O(n) | O(h) | 📝 Stub |
| [Plus One](Easy Problems/plus_one/) | Array/Math | O(n) | O(1) | 📝 Stub |
| [Move Zeroes](Easy Problems/move_zeroes/) | Two Pointers | O(n) | O(1) | 📝 Stub |

### Medium Problems (18 completed, 7 new stubs)

| Problem | Pattern | Time Complexity | Space Complexity | Status |
|---------|---------|-----------------|------------------|--------|
| [Longest Palindromic Substring](Medium Problems/longest_palindromic_substring/) | Two Pointers | O(n²) | O(1) | ✅ Complete |
| [Add Two Numbers](Medium Problems/add_two_numbers/) | Linked List | O(max(n,m)) | O(max(n,m)) | ✅ Complete |
| [Coin Change](Medium Problems/coin_change/) | Dynamic Programming | O(n × m) | O(m) | ✅ Complete |
| [Daily Temperatures](Medium Problems/daily_temperatures/) | Stack | O(n) | O(n) | ✅ Complete |
| [Min Stack](Medium Problems/min_stack/) | Auxiliary Stack | O(1) all ops | O(n) | ✅ Complete |
| [Generate Parentheses](Medium Problems/generate_parenthesis/) | Backtracking | O(4^n/√n) | O(n) | ✅ Complete |
| [Letter Combinations of a Phone Number](Medium Problems/letter_combinations_phone_number/) | Backtracking | O(4^n) | O(4^n) | ✅ Complete |
| [Closest Target in a Circular Array](Medium Problems/closest_target_circle_array/) | Two Pointers | O(n) | O(1) | ✅ Complete |
| [Kth Largest Element in a Stream](Medium Problems/kth_largest_element/) | Heap | O(log k) per add | O(k) | ✅ Complete |
| [Longest Consecutive Sequence](Medium Problems/longest_consecutive_sequence/) | Sort + Scan | O(n log n) | O(n) | ✅ Complete |
| [Longest Increasing Subsequence](Medium Problems/longest_increasing_subsequence/) | Dynamic Programming | O(n²) | O(n) | ✅ Complete |
| [Merge Intervals](Medium Problems/merge_intervals/) | Sort + Greedy | O(n log n) | O(n) | ✅ Complete |
| [Longest Substring Without Repeating Characters](Medium Problems/longest_substring/) | Sliding Window | O(n) | O(min(n,m)) | ✅ Complete |
| [Verifying Alien Dictionary](Medium Problems/verifying_alien_dictionary/) | Hash Map | O(n × m) | O(1) | ✅ Complete |
| [Top K Frequent Elements](Medium Problems/top_k_frequent_elements/) | Frequency Count | O(n log n) | O(n) | ✅ Complete |
| [Group Anagrams](Medium Problems/group_anagrams/) | Hash Map | O(n × k log k) | O(n × k) | ✅ Complete |
| [Spiral Matrix](Medium Problems/spiral_matrix/) | Simulation | O(n × m) | O(1) | ✅ Complete |
| [Product Except Self](Medium Problems/product_except_self/) | Two Pass | O(n) | O(1) | ✅ Complete |
| [Course Schedule](Medium Problems/course_schedule/) | Graph/BFS/DFS | O(V + E) | O(V + E) | 📝 Stub |
| [Clone Graph](Medium Problems/clone_graph/) | Graph/BFS/DFS | O(V + E) | O(V) | 📝 Stub |
| [Word Search](Medium Problems/word_search/) | DFS/Backtracking | O(N × 3^L) | O(L) | 📝 Stub |
| [Subsets](Medium Problems/subsets/) | Backtracking | O(N × 2^N) | O(N) | 📝 Stub |
| [Permutations](Medium Problems/permutations/) | Backtracking | O(N × N!) | O(N) | 📝 Stub |
| [Sort Colors](Medium Problems/sort_colors/) | Two Pointers | O(n) | O(1) | 📝 Stub |
| [Find Minimum in Rotated Sorted Array](Medium Problems/find_minimum_rotated/) | Binary Search | O(log n) | O(1) | 📝 Stub |

---

## Learning Path by Difficulty

### Phase 1: Foundation (Easy Problems)
**Focus**: Basic patterns, simple data structures

1. **Hash Map Basics**
   - [Contains Duplicate](Easy Problems/contains_duplicate/)
   - [Two Sum](Easy Problems/two_sum/) (Hash Map version)

2. **Two Pointers Introduction**
   - [Valid Palindrome](Easy Problems/valid_palindrome/)
   - [Merge Sorted Array](Easy Problems/merge_sorted_array/)
   - [Move Zeroes](Easy Problems/move_zeroes/) (NEW)

3. **Stack Fundamentals**
   - [Valid Parentheses](Easy Problems/valid_parentheses/)

4. **Tree Traversal**
   - [Maximum Depth of Binary Tree](Easy Problems/maximum_depth_binary_tree/)
   - [Count Complete Tree Nodes](Easy Problems/count_complete_tree_nodes/)
   - [Symmetric Tree](Easy Problems/symmetric_tree/) (NEW)
   - [Same Tree](Easy Problems/same_tree/) (NEW)
   - [Invert Binary Tree](Easy Problems/invert_binary_tree/) (NEW)

5. **Dynamic Programming Basics**
   - [Climbing Stairs](Easy Problems/climbing_stairs/)
   - [Maximum Subarray](Easy Problems/maximum_subarray/)

6. **Linked Lists**
   - [Merge Two Sorted Lists](Easy Problems/merge_two_sorted_lists/)
   - [Reverse Linked List](Easy Problems/reverse_linked_list/)

7. **Binary Search**
   - [Binary Search](Easy Problems/binary_search/)
   - [Search Insert Position](Easy Problems/search_insert_position/) (NEW)
   - [First Bad Version](Easy Problems/first_bad_version/) (NEW)

8. **Bit Manipulation (NEW)**
   - [Number of 1 Bits](Easy Problems/number_of_1_bits/) (NEW)
   - [Single Number](Easy Problems/single_number/) (NEW)

9. **Array/Math**
   - [Missing Number](Easy Problems/missing_number/)
   - [Plus One](Easy Problems/plus_one/) (NEW)

### Phase 2: Intermediate (Medium Problems)
**Focus**: Complex patterns, optimization

1. **Advanced Hash Map**
   - [Group Anagrams](Medium Problems/group_anagrams/)
   - [Verifying Alien Dictionary](Medium Problems/verifying_alien_dictionary/)
   - [Top K Frequent Elements](Medium Problems/top_k_frequent_elements/)

2. **Advanced Two Pointers**
   - [Longest Palindromic Substring](Medium Problems/longest_palindromic_substring/)
   - [Three Sum](Medium Problems/three_sum/)
   - [Longest Substring Without Repeating Characters](Medium Problems/longest_substring/)
   - [Sort Colors](Medium Problems/sort_colors/) (NEW)

3. **Stack Applications**
   - [Min Stack](Medium Problems/min_stack/)
   - [Daily Temperatures](Medium Problems/daily_temperatures/)
   - [Final Prices With Discount](Easy Problems/final_prices_with_discount/)

4. **Dynamic Programming**
   - [Coin Change](Medium Problems/coin_change/)
   - [Longest Increasing Subsequence](Medium Problems/longest_increasing_subsequence/)
   - [House Robber](Medium Problems/house_robber/) (TODO)

5. **Backtracking**
   - [Generate Parentheses](Medium Problems/generate_parenthesis/)
   - [Letter Combinations of a Phone Number](Medium Problems/letter_combinations_phone_number/)
   - [Subsets](Medium Problems/subsets/) (NEW)
   - [Permutations](Medium Problems/permutations/) (NEW)

6. **Heap/Priority Queue**
   - [Kth Largest Element in a Stream](Medium Problems/kth_largest_element/)

7. **Greedy Algorithms**
   - [Best Time to Buy and Sell Stock](Easy Problems/max_profit_stocks/)
   - [Merge Intervals](Medium Problems/merge_intervals/)
   - [Jump Game](Medium Problems/jump_game/) (TODO)

8. **BFS/DFS**
   - [Number of Islands](Medium Problems/number_of_islands/)
   - [Word Search](Medium Problems/word_search/) (NEW)

9. **Graph Algorithms (NEW)**
   - [Course Schedule](Medium Problems/course_schedule/) (NEW)
   - [Clone Graph](Medium Problems/clone_graph/) (NEW)

10. **Matrix Problems**
    - [Spiral Matrix](Medium Problems/spiral_matrix/)
    - [Search 2D Matrix](Medium Problems/search_2d_matrix/)
    - [Rotate Image](Medium Problems/rotate_image/)
    - [Container With Most Water](Medium Problems/container_with_most_water/) (needs fix)

11. **Linked Lists Advanced**
    - [Add Two Numbers](Medium Problems/add_two_numbers/)

12. **Array Manipulation**
    - [Product Except Self](Medium Problems/product_except_self/)
    - [Longest Consecutive Sequence](Medium Problems/longest_consecutive_sequence/)
    - [Closest Target in a Circular Array](Medium Problems/closest_target_circle_array/)

13. **Binary Search**
    - [Find Minimum in Rotated Sorted Array](Medium Problems/find_minimum_rotated/) (NEW)

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
