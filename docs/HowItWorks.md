# How It Works - LeetCode Solutions

This document explains the overarching architecture and educational philosophy behind the LeetCode solutions repository, including a comprehensive guide to algorithmic patterns.

---

## Table of Contents
1. [Educational Philosophy](#educational-philosophy)
2. [Repository Architecture](#repository-architecture)
3. [Algorithmic Patterns](#algorithmic-patterns)
4. [Code Style Philosophy](#code-style-philosophy)
5. [Testing Strategy](#testing-strategy)
6. [Learning Path](#learning-path)
7. [Big O Notation Reference](#big-o-notation-reference)
8. [Pattern Deep Dives](#pattern-deep-dives)

---

## Educational Philosophy

This repository is designed to teach algorithmic problem-solving through a structured approach:

1. **Pattern Recognition**: Learn to identify recurring algorithmic patterns
2. **Brute Force First**: Start with the obvious, slow solution
3. **Optimization**: Replace bottlenecks with faster data structures
4. **Complexity Analysis**: Understand time and space trade-offs
5. **Practice**: Apply patterns to new problems

---

## Repository Architecture

### Problem Organization

Each problem is organized in its own directory containing:
- Solution file(s) with the algorithm implementation
- Test file (for practice problems) with test cases
- Comprehensive docstrings explaining the approach

```
two_sum/
├── twoSumBruteForce.py      # O(n²) brute force solution
├── twoSumOnePassHash.py     # O(n) optimized solution
└── test_two_sum.py          # Test suite (practice problems only)
```

### Documentation Structure

```
LeetCode/
├── README.md                    # Project overview and quick start
├── docs/
│   ├── RoadMap.md               # Project status and future work
│   ├── HowItWorks.md            # This file - architecture and patterns
│   ├── ProjectSummary.md        # Feature summary
│   └── ChangeLog.md             # Version history
```

---

## Algorithmic Patterns

### 1. Hash Map Pattern

**When to Use**: O(1) lookup, counting elements, complement problems

**How It Works**:
- Store elements in a hash map for constant-time access
- Trade O(n²) nested loops for O(n) single pass with hash map
- Common use cases: Two Sum, Contains Duplicate, Group Anagrams

**Example Transformation**:
```python
# Brute Force: O(n²)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

# Hash Map: O(n)
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### 2. Two Pointers Pattern

**When to Use**: Sorted arrays, sliding window, removing duplicates

**How It Works**:
- Use two indices to traverse the array
- One pointer moves faster, one slower
- Eliminates need for nested loops in sorted data

**Common Variants**:
- **Sliding Window**: Fixed or variable window size
- **Fast/Slow Pointers**: Detect cycles in linked lists
- **Left/Right Pointers**: Search in sorted arrays

### 3. Stack Pattern

**When to Use**: Matching brackets, monotonic problems, "next greater element"

**How It Works**:
- Last-In-First-Out (LIFO) data structure
- Push elements onto stack, pop when condition met
- Natural for nested structures and reversal problems

**Example**: Valid Parentheses, Daily Temperatures

### 4. Heap / Priority Queue Pattern

**When to Use**: "Top K" problems, streaming minimums/maximums

**How It Works**:
- Always access the minimum (min-heap) or maximum (max-heap) element
- Maintains partial ordering without full sort
- O(log n) insertion and extraction

**Example**: Kth Largest Element in a Stream

### 5. Backtracking Pattern

**When to Use**: Generating all combinations or permutations

**How It Works**:
- Recursively explore all possibilities
- Backtrack (undo) when reaching a dead end
- Build solutions incrementally

**Example**: Generate Parentheses, Letter Combinations of a Phone Number

### 6. Dynamic Programming Pattern

**When to Use**: Overlapping sub-problems, optimal sub-structure

**How It Works**:
- Break problem into smaller sub-problems
- Store solutions to sub-problems (memoization)
- Reuse stored solutions instead of recomputing

**Example**: Coin Change, Climbing Stairs, Longest Increasing Subsequence

### 7. BFS / DFS Pattern

**When to Use**: Tree traversal, grid exploration, connected components

**How It Works**:
- **BFS**: Level-by-level exploration (queue)
- **DFS**: Depth-first exploration (stack/recursion)

**Example**: Number of Islands, Maximum Depth of Binary Tree

---

## Code Style Philosophy

### Variable Naming
- Use descriptive, full variable names
- Avoid single-letter variables except in tight loops
- Example: `current_index` instead of `i`

### Functional Programming Style
- Prefer standalone functions over class-based solutions
- Stateful classes converted to closure-based factories where appropriate
- No class instantiation required to use solutions

### Documentation Standards
- All functions include detailed docstrings
- Inline comments explain each step
- Time and space complexity documented
- Algorithm approach clearly explained

### Comment and Code Spacing
- Comment followed by code: no empty line needed
- Code followed by comment: empty line required
- Indented blocks: single line needs no blank line, multiple lines need separation

---

## Testing Strategy

### Practice Problems
Some problems have test suites with intentionally blank solution files:
- `<name>.py` - Solution stub with docstring
- `test_<name>.py` - Ready-made test cases

Run tests from the problem directory:
```bash
python test_<name>.py
```

When all tests print `PASS`, the solution is correct.

### Direct Execution
Completed solutions can be run directly:
```bash
python twoSumOnePassHash.py
```

---

## Learning Path

### Step 1: Read the Study Guide
Start with `LEETCODE_STUDY_GUIDE.md` to understand the patterns.

### Step 2: Practice with Easy Problems
Begin with easy problems to build confidence:
- Contains Duplicate
- Valid Palindrome
- Binary Search
- Climbing Stairs

### Step 3: Tackle Medium Problems
Apply patterns to more complex problems:
- Two Sum (Hash Map)
- Longest Palindromic Substring
- Generate Parentheses
- Group Anagrams

### Step 4: Analyze Complexity
For each solution, understand:
- Time complexity (Big O)
- Space complexity (memory usage)
- Why the optimization works

### Step 5: Apply to New Problems
Use pattern recognition to solve unfamiliar problems:
1. Read problem carefully
2. Identify constraints
3. Match to known pattern
4. Implement solution
5. Verify with tests

---

## Big O Notation Reference

| Notation | Description | Example |
|----------|-------------|---------|
| O(1) | Constant time - always the same speed | Hash map lookup |
| O(log n) | Logarithmic - gets slightly slower as input doubles | Binary search |
| O(n) | Linear - proportionally slower as input grows | Single loop |
| O(n log n) | Linearithmic - slightly worse than linear | Efficient sorting |
| O(n²) | Quadratic - much slower as input grows | Nested loops |

---

## Pattern Deep Dives

### Array & Hash Table Problems

#### Two Sum (Brute Force vs Optimized)

**Related Problems:**
- LeetCode #1: Two Sum

**Approaches:**

**Brute Force Approach (`twoSumBruteForce.py`)**
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Principle:** Nested loops to check all pairs

**When to Use:**
- Small datasets
- When space is extremely limited
- Interview warm-up to show understanding before optimization

**Hash Map Approach (`twoSumOnePassHash.py`)**
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Principle:** Trade space for time using a hash map

**Key Insights:**
- **Complement Pattern:** For each number, calculate `complement = target - current_number`
- **Single Pass:** Store numbers as you iterate, checking if complement exists
- **Hash Map Usage:** Key = number value, Value = index position

**Tips:**
```python
# Always check if complement exists BEFORE adding current number
if complement in numMap:
    return [numMap[complement], i]
numMap[num] = i  # Add after checking
```

#### Top K Frequent Elements

**Related Problems:**
- LeetCode #347: Top K Frequent Elements

**File:** `topKfreqElems.py`

**Approach:**
- **Time Complexity:** O(n log n) due to sorting
- **Space Complexity:** O(n)

**Pattern: Frequency Counting + Sorting**

**Steps:**
1. **Count frequencies** using a hash map: `count[num] = 1 + count.get(num, 0)`
2. **Convert to sortable format:** Create list of `[frequency, number]` pairs
3. **Sort by frequency:** Natural sort puts lowest first
4. **Extract top K:** Pop from end K times

**Key Insights:**
- `dict.get(key, default)` prevents KeyError when counting
- Sorting `[count, num]` pairs sorts by count first (Python's natural tuple sorting)
- Popping from end gets highest frequencies

**Optimization Opportunity:**
- Use **Bucket Sort** for O(n) time complexity
- Use **Heap** for O(n log k) time complexity (better for small k)

#### Longest Consecutive Sequence

**Related Problems:**
- LeetCode #128: Longest Consecutive Sequence

**File:** `longestConseqSeq.py`

**Approach:**
- **Time Complexity:** O(n log n) due to sorting
- **Space Complexity:** O(n) for set conversion

**Pattern: Sort + Linear Scan**

**Steps:**
1. **Remove duplicates:** Convert to set, then back to list
2. **Sort the array:** Makes consecutive numbers adjacent
3. **Track sequences:** Count consecutive differences of 1
4. **Update maximum:** Keep track of longest sequence

**Key Insights:**
- Check if `nums[i+1] - nums[i] == 1` for consecutive numbers
- Reset counter when sequence breaks
- Duplicates must be removed first

**Optimization:**
- Use **Hash Set** approach for O(n) time without sorting
- Only start counting from sequence beginnings (num-1 not in set)

#### Verifying Alien Dictionary

**Related Problems:**
- LeetCode #953: Verifying an Alien Dictionary

**File:** `verifyingAlienDictionary.py`

**Approach:**
- **Time Complexity:** O(n × m) where n = words, m = max word length
- **Space Complexity:** O(1) - fixed alphabet size

**Pattern: Custom Ordering with Hash Map**

**Steps:**
1. **Create order mapping:** `{char: position for position, char in enumerate(order)}`
2. **Compare character by character:** Check each position across all words
3. **Handle edge cases:** Shorter words should come before longer words with same prefix

**Key Insights:**
- Dictionary comprehension for O(1) character lookups
- Treat missing characters (past word length) as `-1` (comes first)
- If all characters at position are different and sorted, return True early
- If previous character > current character, immediately return False

**Tips:**
- Position-by-position comparison is more efficient than word-by-word
- Early termination when all words differ at a position

### Linked List Problems

#### Merge Two Sorted Linked Lists

**Related Problems:**
- LeetCode #21: Merge Two Sorted Lists

**File:** `mergeTwoSortedLinkedLists.py`

**Approach:**
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1) - in-place merging

**Pattern: Two Pointer + Dummy Node**

**Key Techniques:**

**Dummy Node Pattern**
```python
head = ListNode(0)  # Dummy node
tail = head         # Tail pointer
# ... merge logic ...
return head.next    # Skip dummy
```

**Why Dummy Nodes?**
- Eliminates edge case handling for empty lists
- Simplifies code - no special first element logic
- Common pattern in linked list problems

**Steps:**
1. Create dummy head and tail pointer
2. Compare values from both lists
3. Attach smaller node to tail, advance that list's pointer
4. Move tail forward
5. Attach remaining nodes from non-empty list

**Tips:**
- Always use dummy nodes for list construction
- Remember to return `head.next`, not `head`
- Handle remaining elements efficiently: `tail.next = list1 if list1 else list2`

#### Add Two Numbers (Linked Lists)

**Related Problems:**
- LeetCode #2: Add Two Numbers

**File:** `addTwoNumbers.py`

**Approach:**
- **Time Complexity:** O(max(n, m))
- **Space Complexity:** O(max(n, m))

**Pattern: Digit-by-Digit Addition with Carry**

**Key Concepts:**

**Carry Management**
```python
sum = carry + x + y
carry = sum // 10      # Integer division for carry
digit = sum % 10       # Modulo for current digit
```

**Steps:**
1. Create dummy node for result
2. Initialize carry = 0
3. While either list has nodes OR carry exists:
   - Get values (0 if node is None)
   - Calculate sum + carry
   - Extract new carry and digit
   - Create new node with digit
4. Don't forget final carry!

**Critical Tips:**
- Use `x = l1.val if l1 is not None else 0` for safe value extraction
- Continue loop while `l1 OR l2 OR carry` (not just while both exist)
- Handle final carry: `if carry > 0: current.next = ListNode(carry)`

**Common Mistakes:**
- Forgetting to add final carry node
- Not handling lists of different lengths
- Advancing pointers incorrectly

### Stack & Queue Problems

#### Min Stack

**Related Problems:**
- LeetCode #155: Min Stack

**File:** `minStack.py`

**Approach:**
- **Time Complexity:** O(1) for all operations
- **Space Complexity:** O(n)

**Pattern: Auxiliary Stack for Metadata**

**Key Insight:**
- Maintain **two parallel stacks**:
  1. `stack`: stores actual values
  2. `min_stack`: stores minimum at each state

**Implementation:**
```python
def push(self, val):
    self.stack.append(val)
    self.min_stack.append(min(val, self.min_stack[-1]))

def pop(self):
    self.stack.pop()
    self.min_stack.pop()  # Keep in sync!

def getMin(self):
    return self.min_stack[-1]  # O(1) access
```

**Why This Works:**
- Each position in `min_stack` stores the minimum of all elements up to that point
- When popping, both stacks stay synchronized
- Sentinel value (`float('inf')`) prevents empty stack errors

**General Principle:**
- **Auxiliary data structures** can maintain metadata (min, max, frequency) in O(1)
- Trade space for time complexity improvement
- Keep structures synchronized during modifications

### Tree Problems

#### Count Complete Tree Nodes

**Related Problems:**
- LeetCode #222: Count Complete Tree Nodes

**File:** `countCompleteTreeNodes.py`

**Approach:**
- **Time Complexity:** O(n) - simple recursive
- **Space Complexity:** O(h) - recursion stack

**Pattern: Tree Recursion**

**Basic Recursive Formula:**
```python
count(node) = 1 + count(left) + count(right)
```

**Steps:**
1. Base case: if node is None, return 0
2. Recursive case: 1 (current) + left subtree count + right subtree count

**Optimization for Complete Trees:**
- Can achieve O(log²n) by checking if tree is perfect
- Compare left height vs right height
- If equal: use formula `2^h - 1`

**Key Insights:**
- Simple recursion works but isn't optimal for complete trees
- Complete tree properties allow mathematical shortcuts
- Always check for base cases first

### Backtracking & Recursion

#### Generate Parentheses

**Related Problems:**
- LeetCode #22: Generate Parentheses

**File:** `generateParenthesis.py`

**Approach:**
- **Time Complexity:** O(4^n / √n) - Catalan number
- **Space Complexity:** O(n) - recursion depth

**Pattern: Backtracking with Pruning**

**Pruning Rules (Critical!):**

1. **Rule 1 - Bounds Check:**
   ```python
   if left > n or right > n or right > left:
       return  # Prune invalid branches
   ```

2. **Rule 2 - Goal State:**
   ```python
   if left == n and right == n:
       result.append(current)
       return
   ```

3. **Rule 3 - Exploration Order:**
   ```python
   backtrack(left + 1, right, current + "(")  # Try opening first
   backtrack(left, right + 1, current + ")")  # Then closing
   ```

**Key Insights:**
- **Never have more closing than opening:** `right > left` is invalid
- **Prune early:** Don't explore invalid branches
- **DFS with constraints:** Backtracking explores all valid paths

**Backtracking Template:**
```python
def backtrack(state, path):
    if invalid(state):
        return  # Prune
    if is_goal(state):
        result.append(path)
        return
    for next_state in get_next_states(state):
        backtrack(next_state, path + next_choice)
```

#### Letter Combinations of a Phone Number

**Related Problems:**
- LeetCode #17: Letter Combinations of a Phone Number

**File:** `letterCombinationsOfAPhoneNumber.py`

**Approach:**
- **Time Complexity:** O(4^n) worst case
- **Space Complexity:** O(4^n) for output

**Pattern: Iterative Cartesian Product**

**Key Technique - List Comprehension:**
```python
ans = [a + b for a in ans for b in s]
```

**How It Works:**
- Start with `ans = [""]`
- For each digit, multiply combinations by letters
- Example: `"23"` → `[""]` → `["a","b","c"]` → `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Steps:**
1. Create keypad mapping: `["", "", "abc", "def", ...]`
2. Initialize result with empty string
3. For each digit, cross-multiply current results with digit's letters

**Alternative Approach:**
- Can also use backtracking/DFS
- Iterative approach is more elegant for this problem

### Heap & Priority Queue

#### Kth Largest Element in Stream

**Related Problems:**
- LeetCode #703: Kth Largest Element in a Stream

**File:** `kthLargestElement.py`

**Approach:**
- **Time Complexity:** O(log k) per add operation
- **Space Complexity:** O(k)

**Pattern: Min Heap of Size K**

**Key Insight:**
- Maintain a **min heap of exactly k elements**
- The root (minimum) of this heap is the kth largest overall
- Smaller elements get pushed out

**Implementation:**
```python
def add(self, val):
    if len(self.min_heap) < self.k or self.min_heap[0] < val:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
    return self.min_heap[0]
```

**Why Min Heap?**
- Min heap keeps smallest element at top
- For "kth largest", we want to remove smallest elements
- Top of heap = kth largest element

**Heap Selection Guide:**
- **Kth largest** → Use min heap (remove small elements)
- **Kth smallest** → Use max heap (remove large elements)

**Tips:**
- Python's `heapq` is always a min heap
- For max heap: negate values or use `(-val, val)` tuples

### Sorting & Searching

#### Search in 2D Matrix

**Related Problems:**
- LeetCode #74: Search a 2D Matrix (simplified version)

**File:** `search2DMatrix.py`

**Approach:**
- **Time Complexity:** O(n × m) - linear search
- **Space Complexity:** O(1)

**Current Pattern: Linear Search**
```python
for row in matrix:
    if target in row:
        return True
```

**Optimization Opportunities:**

**Binary Search Approach (O(log(n×m)))**
- Treat 2D matrix as 1D sorted array
- Use binary search with index conversion
- `mid_row = mid // cols`, `mid_col = mid % cols`

**Staircase Search (O(n + m))**
- Start at top-right or bottom-left
- Move left if target smaller, down if larger
- Works for row-sorted and column-sorted matrices

**Key Principle:**
- Exploit sorted properties for better than O(n×m)
- Always consider if binary search applies

#### Merge Intervals

**Related Problems:**
- LeetCode #56: Merge Intervals

**File:** `mergeIntervals.py`

**Approach:**
- **Time Complexity:** O(n log n) - dominated by sorting
- **Space Complexity:** O(n)

**Pattern: Sort + Greedy Merge**

**Steps:**
1. **Sort intervals** by start time: `intervals.sort()`
2. **Initialize** with first interval: `currentS, currentE = intervals[0]`
3. **Iterate** through remaining intervals:
   - If no overlap (`currentE < intervalS`): add current, start new interval
   - If overlap: extend current interval (`currentE = max(currentE, intervalE)`)
4. **Don't forget** to add the last interval!

**Key Insights:**
```python
# No overlap condition
if currentE < intervalS:
    mergedI.append([currentS, currentE])
    currentS, currentE = intervalS, intervalE

# Overlap condition - extend
else:
    currentE = max(currentE, intervalE)
```

**Why Sorting Helps:**
- Guarantees we process intervals in order
- Only need to check current interval vs next
- No need to check backwards

**Common Mistakes:**
- Forgetting to add final interval after loop
- Not using `max()` when merging (intervals can be nested)

### Greedy Algorithms

#### Best Time to Buy and Sell Stock (Multiple Transactions)

**Related Problems:**
- LeetCode #122: Best Time to Buy and Sell Stock II

**File:** `maxProfitStocks.py`

**Approach:**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

**Pattern: Greedy - Capture All Upward Movements**

**Key Insight:**
```python
# Iterate backwards
for i in range(len(prices)-1, 0, -1):
    if prices[i] > prices[i-1]:
        profit += prices[i] - prices[i-1]
```

**Why This Works:**
- Any upward price movement is profit opportunity
- Can buy and sell same day (no cooldown in this variant)
- Equivalent to summing all positive differences

**Visualization:**
```
Prices: [1, 6, 4, 7, 3, 9]
Profit: (6-1) + (7-4) + (9-3) = 5 + 3 + 6 = 14
```

**Greedy Principle:**
- Make locally optimal choice (take every profit)
- Leads to globally optimal solution
- No need for complex DP

### Two Pointer Technique

#### Merge Sorted Array (In-Place)

**Related Problems:**
- LeetCode #88: Merge Sorted Array

**File:** `mergeSortedArray.py`

**Approach:**
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1) - in-place

**Pattern: Two Pointers from End**

**Key Insight - Work Backwards:**
```python
nums1lastValue = m - 1      # Last element of nums1
nums2lastValue = n - 1      # Last element of nums2
nums1lastIndex = m + n - 1  # Last position in merged array
```

**Why Backwards?**
- Avoids overwriting unprocessed elements
- Empty space is at the end of nums1
- Can place largest elements first

**Algorithm:**
```python
while nums2lastValue >= 0:
    if nums1lastValue >= 0 and nums1[nums1lastValue] > nums2[nums2lastValue]:
        nums1[nums1lastIndex] = nums1[nums1lastValue]
        nums1lastValue -= 1
    else:
        nums1[nums1lastIndex] = nums2[nums2lastValue]
        nums2lastValue -= 1
    nums1lastIndex -= 1
```

**Key Points:**
- Only need to continue while nums2 has elements
- If nums2 is exhausted, nums1 elements are already in place
- Always decrement the placement index

---

## General Problem-Solving Principles

### 1. **Time-Space Tradeoff**
- Hash maps trade O(n) space for O(1) lookup time
- Auxiliary stacks/arrays can maintain metadata efficiently
- Consider if extra space can simplify logic or improve performance

### 2. **Dummy Nodes in Linked Lists**
- Eliminates edge cases for empty lists
- Simplifies insertion/deletion logic
- Always return `dummy.next`

### 3. **Sorting as Preprocessing**
- Many problems become easier after sorting
- O(n log n) sort + O(n) scan = O(n log n) total
- Enables two-pointer techniques

### 4. **Backtracking Template**
```python
def backtrack(state, path):
    if invalid(state):
        return  # Prune
    if is_goal(state):
        result.append(path)
        return
    for next_state in possible_states:
        backtrack(next_state, path + choice)
```

### 5. **Greedy vs Dynamic Programming**
- **Greedy:** Local optimal → Global optimal (if problem has greedy property)
- **DP:** Overlapping subproblems + optimal substructure
- Try greedy first if it seems to work, prove correctness

### 6. **Heap Selection**
- Kth largest → Min heap of size k
- Kth smallest → Max heap of size k
- Top K elements → Heap of size k

### 7. **Two Pointer Patterns**
- **Same direction:** Fast/slow pointers (cycle detection)
- **Opposite direction:** Start/end pointers (two sum in sorted array)
- **Sliding window:** Expand/contract window for subarrays

### 8. **Recursion Best Practices**
- Always define base case first
- Ensure progress toward base case
- Consider iterative alternative if stack depth is concern

### 9. **Edge Cases to Consider**
- Empty input
- Single element
- Duplicates
- Negative numbers
- Integer overflow
- Null/None values

### 10. **Optimization Strategy**
1. Start with brute force (shows understanding)
2. Identify bottlenecks
3. Consider data structures (hash, heap, stack)
4. Look for patterns (two pointer, sliding window, etc.)
5. Analyze time/space complexity

---

## Quick Reference: Problem → Pattern

| Problem | Primary Pattern | Key Data Structure | Time Complexity |
|---------|----------------|-------------------|-----------------|
| Two Sum | Hash Map | Dictionary | O(n) |
| Top K Frequent | Frequency Count + Sort | Hash Map + Array | O(n log n) |
| Longest Consecutive | Sort + Scan | Set + Array | O(n log n) |
| Alien Dictionary | Custom Ordering | Hash Map | O(n × m) |
| Merge Two Lists | Two Pointer | Dummy Node | O(n + m) |
| Add Two Numbers | Digit Processing | Linked List | O(max(n,m)) |
| Min Stack | Auxiliary Stack | Two Stacks | O(1) all ops |
| Count Tree Nodes | Tree Recursion | Tree | O(n) |
| Generate Parentheses | Backtracking | Recursion | O(4^n/√n) |
| Phone Number Combos | Cartesian Product | List Comprehension | O(4^n) |
| Kth Largest | Min Heap | Heap | O(log k) |
| Search 2D Matrix | Linear Search | 2D Array | O(n × m) |
| Merge Intervals | Sort + Greedy | Array | O(n log n) |
| Stock Profit | Greedy | Array | O(n) |
| Merge Sorted Array | Two Pointer (Reverse) | Array | O(n + m) |

---

## Study Tips

1. **Pattern Recognition:** Focus on recognizing patterns rather than memorizing solutions
2. **Practice Variations:** Solve similar problems to reinforce patterns
3. **Optimize Incrementally:** Start with working solution, then optimize
4. **Explain Out Loud:** If you can't explain it, you don't understand it
5. **Time Yourself:** Practice under interview conditions
6. **Review Mistakes:** Keep a log of errors and misunderstandings
7. **Draw It Out:** Visualize data structures and algorithm flow
8. **Test Edge Cases:** Always consider empty, single, and extreme inputs

---

## Additional Resources

- **LeetCode Patterns:** Group problems by pattern, not by topic
- **Time Complexity Cheat Sheet:** Know Big-O for common operations
- **Data Structure Operations:** Memorize time/space for insert, delete, search
- **Python Built-ins:** Know `collections`, `heapq`, `bisect` modules

---

## Conclusion

This repository is designed as a comprehensive learning resource for algorithmic problem-solving. By studying the patterns, understanding the optimizations, and practicing with the provided problems, you'll develop the skills needed to tackle any algorithmic challenge.
