
Think of these as the equivalent of:

```text
Math -> Formula
DSA -> Pattern + Template
```

Don't memorize 300 questions. Memorize ~10-15 patterns.

---

# Formula 1: Two Pointers

### Use When

```text
- Two strings
- Sorted array
- In-place modification
- Pair searching
```

### Template

```python
left = 0
right = len(nums) - 1

while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

### Questions

* Move Zeroes
* Is Subsequence
* Valid Palindrome
* Container With Most Water

---

# Formula 2: Fast & Slow Pointers

### Use When

```text
Linked List
Cycle Detection
Middle Element
```

### Template

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Questions

* Linked List Cycle
* Middle of Linked List

---

# Formula 3: Sliding Window (Fixed)

### Use When

```text
Subarray of size k
Average
Maximum
Minimum
```

### Template

```python
window_sum = sum(nums[:k])

for i in range(k, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i-k]
```

### Questions

* Maximum Average Subarray

---

# Formula 4: Sliding Window (Variable)

### Use When

```text
Longest
Shortest
Substring
Subarray
```

### Template

```python
left = 0

for right in range(len(nums)):

    while condition:
        left += 1
```

### Questions

* Longest Substring Without Repeating Characters

---

# Formula 5: HashMap Frequency Count

### Use When

```text
Count frequency
Compare frequency
Duplicates
```

### Template

```python
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

### Questions

* Valid Anagram
* Ransom Note
* Top K Frequent Elements

---

# Formula 6: HashSet Lookup

### Use When

```text
Need O(1) lookup
Duplicate detection
Unique elements
```

### Template

```python
seen = set()

for x in nums:
    if x in seen:
        return True

    seen.add(x)
```

### Questions

* Contains Duplicate
* Happy Number

---

# Formula 7: Prefix Sum

### Use When

```text
Range Sum
Running Total
Subarray Sum
```

### Template

```python
prefix = [0] * (len(nums) + 1)

for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]
```

### Questions

* Running Sum
* Pivot Index
* Subarray Sum Equals K

---

# Formula 8: Binary Search

### Use When

```text
Sorted Array
Searching
Find Position
```

### Template

```python
left = 0
right = len(nums) - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1
```

### Questions

* Binary Search
* Search Insert Position

---

# Formula 9: DFS (Tree)

### Use When

```text
Explore Deep First
Tree Traversal
```

### Template

```python
def dfs(node):

    if not node:
        return

    dfs(node.left)
    dfs(node.right)
```

### Questions

* Maximum Depth of Binary Tree
* Same Tree

---

# Formula 10: BFS (Tree)

### Use When

```text
Level Order
Shortest Path
Level by Level
```

### Template

```python
from collections import deque

q = deque([root])

while q:

    node = q.popleft()

    if node.left:
        q.append(node.left)

    if node.right:
        q.append(node.right)
```

### Questions

* Binary Tree Level Order Traversal

---

# Formula 11: Heap

### Use When

```text
Top K
Smallest
Largest
Priority
```

### Template

```python
import heapq

heap = []

heapq.heappush(heap, x)

smallest = heapq.heappop(heap)
```

### Questions

* Kth Largest Element
* Top K Frequent Elements

---

# Formula 12: Backtracking

### Use When

```text
Generate All
Permutations
Combinations
Subsets
```

### Template

```python
def backtrack(path):

    if condition:
        result.append(path[:])
        return

    for choice in choices:

        path.append(choice)

        backtrack(path)

        path.pop()
```

### Questions

* Subsets
* Permutations

---

# Formula 13: Graph DFS

### Use When

```text
Connected Components
Traversal
```

### Template

```python
def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)
```

---

# Formula 14: Graph BFS

### Use When

```text
Shortest Path
Level Traversal
```

### Template

```python
from collections import deque

q = deque([start])

visited = {start}

while q:

    node = q.popleft()

    for nei in graph[node]:

        if nei not in visited:

            visited.add(nei)

            q.append(nei)
```

---

# Formula 15: Dynamic Programming

### Use When

```text
Repeated Work
Optimization
Count Ways
```

### Template

```python
dp = [0] * (n + 1)

dp[0] = base_case

for i in range(1, n + 1):
    dp[i] = ...
```

### Questions

* Climbing Stairs
* House Robber




