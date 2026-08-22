# Path Sum III (LeetCode 437)

You are given the **root** of a binary tree and an integer `targetSum`.

Return the number of paths where the sum of the values along the path equals `targetSum`.

The path:

- Does not need to start at the root.
- Does not need to end at a leaf.
- Must always move **downward**, from parent to child.

For example:

```text
        10
       /  \
      5   -3
     / \    \
    3   2    11
   / \   \
  3  -2   1
```

For:

```text
targetSum = 8
```

the valid paths are:

```text
5 → 3

5 → 2 → 1

-3 → 11
```

Therefore:

```text
Answer = 3
```



## Example 1

```text
Input:

root = [10,5,-3,3,2,null,11,3,-2,null,1]

targetSum = 8

Output:

3
```

Explanation:

```text
5 → 3

5 → 2 → 1

-3 → 11
```

All three paths have a sum of `8`.



## Example 2

```text
Input:

root = [5,4,8,11,null,13,4,7,2,null,null,5,1]

targetSum = 22

Output:

3
```



## Example 3

```text
Input:

root = []

targetSum = 0

Output:

0
```

Explanation:

```text
There are no nodes.

Therefore, there are no valid paths.
```



## Constraints

```text
0 <= Number of Nodes <= 1000

-10^9 <= Node.val <= 10^9

-1000 <= targetSum <= 1000
```



# Pattern

```text
Binary Tree

DFS

Prefix Sum

Hash Map

Path Tracking
```



# Recognition

Use this pattern when the problem asks:

- Count paths with a particular sum
- Paths can start anywhere
- Paths must move downward
- Values can be positive, zero, or negative
- Find the number of subarrays/subpaths with a target sum

The key clue is:

```text
Count paths with sum = targetSum
```

while the path does not have to start at the root.



# Brute Force

## Intuition

For every node, treat it as a possible starting point.

Then perform another DFS to find all downward paths starting from that node.

This means we repeatedly traverse parts of the tree.

## Brute Force Code

```python

class Solution(object):
    def pathSum(self, root, targetSum):

        def find_paths(node, remaining):
            if node is None:
                return 0

            remaining -= node.val

            count = 0

            if remaining == 0:
                count += 1

            count += find_paths(node.left, remaining)
            count += find_paths(node.right, remaining)

            return count

        def traverse(node):
            if node is None:
                return 0

            count = find_paths(node, targetSum)

            count += traverse(node.left)
            count += traverse(node.right)

            return count

        return traverse(root)
```

## Complexity

```text
Time : O(n²)
```

in the worst case.

```text
Space : O(h)
```

for the recursion stack.



# Optimal Approach (Prefix Sum + Hash Map)

## Key Observation

Instead of starting a new path from every node, we can use **prefix sums**.

Suppose the path from the root to the current node has sum:

```text
current_sum
```

We want a path whose sum is:

```text
targetSum
```

Suppose an earlier prefix had sum:

```text
previous_sum
```

Then:

```text
current_sum - previous_sum = targetSum
```

Therefore:

```text
previous_sum = current_sum - targetSum
```

So while traversing the tree, we only need to check:

```python
prefix.get(current_sum - targetSum, 0)
```

This tells us how many earlier prefixes can be removed from the current prefix to form a path whose sum equals `targetSum`.



# Prefix Sum Intuition

Consider:

```text
10 → 5 → 3
```

The prefix sums are:

```text
10

10 + 5 = 15

10 + 5 + 3 = 18
```

Suppose:

```text
targetSum = 8
```

At node `3`:

```text
current_sum = 18
```

We need an earlier prefix:

```text
18 - previous_sum = 8
```

Therefore:

```text
previous_sum = 10
```

We have already seen prefix sum `10`.

Removing that prefix gives:

```text
5 + 3 = 8
```

So:

```text
5 → 3
```

is a valid path.

---

# The Hash Map

We maintain:

```python
prefix
```

where:

```text
key   = prefix sum

value = number of times that prefix sum has appeared
```

For example:

```text
prefix = {
    0: 1,
    10: 1,
    15: 1,
    18: 1
}
```

The value represents how many times a particular prefix sum has appeared on the **current root-to-node path**.



# Why `prefix = {0: 1}`?

We initialize:

```python
prefix = {0: 1}
```

This represents an empty path whose sum is:

```text
0
```

It is necessary for paths that start directly at the root.

For example:

```text
5
```

with:

```text
targetSum = 5
```

At node `5`:

```text
current_sum = 5
```

We need:

```text
current_sum - targetSum

= 5 - 5

= 0
```

Because:

```text
prefix[0] = 1
```

we correctly count:

```text
5
```

as a valid path.



# Algorithm

1. Initialize:

```python
prefix = {0: 1}
```

2. Start DFS with:

```python
current_sum = 0
```

3. At each node:

```python
current_sum += node.val
```

4. Calculate:

```python
current_sum - targetSum
```

5. Look up how many times this prefix sum has appeared:

```python
count = prefix.get(current_sum - targetSum, 0)
```

6. Add the current prefix sum to the hash map:

```python
prefix[current_sum] = prefix.get(current_sum, 0) + 1
```

7. Recursively traverse the left and right subtrees.

8. Remove the current prefix sum before returning:

```python
prefix[current_sum] -= 1
```

9. Return the total count.



# Code

```python
class Solution(object):

    def pathSum(self, root, targetSum):

        prefix = {0: 1}

        def traverse(node, current_sum):

            if node is None:
                return 0

            current_sum += node.val

            count = prefix.get(current_sum - targetSum, 0)

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            count += traverse(node.left, current_sum)
            count += traverse(node.right, current_sum)

            prefix[current_sum] -= 1

            return count

        return traverse(root, 0)
```



# Walkthrough

## Example

```text
        10
       /  \
      5   -3
     / \    \
    3   2    11
   / \   \
  3  -2   1
```

Target:

```text
8
```

Initially:

```python
prefix = {0: 1}
```



## Node 10

```text
current_sum = 0 + 10

current_sum = 10
```

We need:

```text
10 - 8 = 2
```

Check:

```text
prefix[2]
```

It doesn't exist.

So:

```text
count = 0
```

Add `10`:

```text
prefix = {
    0: 1,
    10: 1
}
```



## Node 5

```text
current_sum = 10 + 5

current_sum = 15
```

We need:

```text
15 - 8 = 7
```

There is no prefix sum `7`.

So:

```text
count = 0
```

Add `15`:

```text
prefix = {
    0: 1,
    10: 1,
    15: 1
}
```



## Node 3

```text
current_sum = 15 + 3

current_sum = 18
```

We need:

```text
18 - 8 = 10
```

We have:

```text
prefix[10] = 1
```

Therefore:

```text
count = 1
```

This represents the path:

```text
5 → 3
```

because:

```text
18 - 10 = 8
```

Add `18`:

```text
prefix = {
    0: 1,
    10: 1,
    15: 1,
    18: 1
}
```



# Node 3's Left Child

The next node is another `3`.

```text
current_sum = 18 + 3

current_sum = 21
```

We need:

```text
21 - 8 = 13
```

There is no prefix sum `13`.

So:

```text
count = 0
```



# Backtracking

After finishing the subtree of node `3`, we execute:

```python
prefix[current_sum] -= 1
```

For example:

```text
prefix[21] -= 1
```

This removes the prefix sum belonging to that node.

This is important because the prefix map should contain only prefix sums belonging to the **current path**.



# Why Do We Remove the Prefix Sum?

Consider:

```text
        10
       /  \
      5    2
```

When traversing the left side:

```text
10 → 5
```

the prefix map contains:

```text
0
10
15
```

When we move to the right side:

```text
10 → 2
```

the prefix sum `15` from the left subtree must not be visible.

Otherwise, we could accidentally create a path using nodes from different branches.

Therefore, after finishing a node:

```python
prefix[current_sum] -= 1
```

restores the map to the state it had before entering that node.



# Backtracking

The traversal follows this pattern:

```text
Add current prefix sum

↓

Explore left subtree

↓

Explore right subtree

↓

Remove current prefix sum
```

This is called **backtracking**.

The hash map always represents:

```text
Prefix sums on the current root-to-node path
```

not the entire tree.



# Why Does `current_sum - targetSum` Work?

Suppose:

```text
previous_sum = 10

current_sum = 18
```

Then the path between those two prefix points has sum:

```text
18 - 10 = 8
```

Therefore, if:

```text
targetSum = 8
```

we need to find:

```text
18 - 8 = 10
```

in the prefix map.

That is exactly what this line does:

```python
count = prefix.get(current_sum - targetSum, 0)
```



# Handling Duplicate Prefix Sums

The hash map stores **counts**, not just whether a prefix sum exists.

For example:

```text
prefix = {
    0: 1,
    5: 2
}
```

means the prefix sum `5` has appeared twice on the current path.

If:

```text
current_sum - targetSum = 5
```

then both occurrences can potentially create a valid path.

Therefore:

```python
count = prefix.get(current_sum - targetSum, 0)
```

adds the correct number of paths.



# Dry Run

For the path:

```text
10 → 5 → 3
```

with:

```text
targetSum = 8
```

| Node | `current_sum` | Needed Prefix | Found | Count |
|------|---------------|---------------|-------|-------|
| 10 | 10 | 2 | 0 | 0 |
| 5 | 15 | 7 | 0 | 0 |
| 3 | 18 | 10 | 1 | 1 |

The path:

```text
5 → 3
```

is counted.



# Complexity

```text
Time : O(n)
```

Every node is visited once.

Hash map operations are `O(1)` on average.

```text
Space : O(h)
```

The prefix map and recursion stack contain information for the current root-to-node path.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```



# Common Mistakes

### ❌ Forgetting `prefix = {0: 1}`

Without:

```python
prefix = {0: 1}
```

paths that start at the root may not be counted.



### ❌ Storing Only Whether a Prefix Exists

Wrong:

```python
prefix[current_sum] = True
```

Multiple occurrences of the same prefix sum can represent multiple valid paths.

We need:

```python
prefix[current_sum] = prefix.get(current_sum, 0) + 1
```



### ❌ Forgetting to Backtrack

Wrong:

```python
count += traverse(node.left, current_sum)
count += traverse(node.right, current_sum)

return count
```

We must remove the current prefix before returning:

```python
prefix[current_sum] -= 1
```

Otherwise prefix sums from one branch can incorrectly affect another branch.



### ❌ Using Only the Current Node Value

The problem is about the sum of an entire downward path.

We need:

```python
current_sum += node.val
```

to maintain the prefix sum from the root.



### ❌ Assuming Values Are Positive

Node values can be negative:

```text
-10^9 <= Node.val <= 10^9
```

So we cannot use a sliding-window approach based on the sum only increasing.

Prefix sums work with positive and negative values.



# Similar Problems

- Path Sum
- Path Sum II
- Subarray Sum Equals K
- Binary Tree Maximum Path Sum
- Sum Root to Leaf Numbers



# Interview Takeaway

## Recognition

```text
Binary Tree

DFS

Prefix Sum

Hash Map

Backtracking
```

## Core Trick

```text
Maintain Current Prefix Sum

↓

Need a Previous Prefix Sum

↓

current_sum - previous_sum = targetSum

↓

Therefore:

previous_sum = current_sum - targetSum

↓

Look It Up in Hash Map

↓

Count Matching Prefixes

↓

Add Current Prefix Sum

↓

Traverse Children

↓

Remove Current Prefix Sum

↓

Return Total Count
```
