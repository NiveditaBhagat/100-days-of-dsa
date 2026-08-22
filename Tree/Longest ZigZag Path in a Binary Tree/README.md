
# Longest ZigZag Path in a Binary Tree (LeetCode 1372)

You are given the **root** of a binary tree.

A ZigZag path is a path where the direction alternates between **left** and **right** at every step.

For example:

```text
Left → Right → Left → Right
```

or:

```text
Right → Left → Right → Left
```

The ZigZag length is the number of **edges** in the path.

A single node has a ZigZag length of:

```text
0
```



## Example 1

```text
Input:

root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]

Output:

3
```

Explanation:

```text
The longest ZigZag path is:

Right → Left → Right
```

Therefore:

```text
ZigZag Length = 3
```



## Example 2

```text
Input:

root = [1,1,1,null,1,null,null,1,1,null,1]

Output:

4
```

Explanation:

```text
The longest ZigZag path is:

Left → Right → Left → Right
```

Therefore:

```text
ZigZag Length = 4
```


## Example 3

```text
Input:

root = [1]

Output:

0
```

Explanation:

```text
There is only one node.

There are no edges to traverse.

Therefore, the ZigZag length is 0.
```



## Constraints

```text
1 <= Number of Nodes <= 5 * 10^4

1 <= Node.val <= 100
```

---

# Pattern

```text
Binary Tree

DFS

Recursion

State Tracking

Longest Path
```



# Recognition

Use this pattern when the problem involves:

- Traversing a binary tree
- Alternating between left and right
- Finding the longest path
- Keeping track of the previous direction
- Maintaining information while moving down the tree



# Brute Force


## Intuition

We can start a ZigZag traversal from every node.

For every node, try both possible starting directions:

```text
Left
```

and:

```text
Right
```

Then continue alternating directions.



## Algorithm

1. Start a ZigZag traversal from every node.
2. Try starting with the left direction.
3. Try starting with the right direction.
4. Continue alternating directions.
5. Keep track of the longest path.



## Why is it Not Ideal?

The same subtrees can be traversed repeatedly from different starting nodes.

This can lead to unnecessary repeated work.



## Complexity

```text
Time : O(n^2) in the worst case

Space : O(h)
```

where `h` is the height of the tree.



# Optimal Approach

## Key Observation

At every node, we need to know how long the current ZigZag path is depending on the direction we need to take next.

We maintain two values:

```text
left_count

right_count
```

`left_count` represents the length of the ZigZag path if the next move is expected to be **left**.

`right_count` represents the length of the ZigZag path if the next move is expected to be **right**.



# Why Do We Need Two Counts?

Suppose we have:

```text
        1
       /
      2
       \
        3
```

The path is:

```text
Left → Right
```

After moving left from `1` to `2`, the next move must be right.

Therefore, the state changes from:

```text
left_count
```

to:

```text
right_count = left_count + 1
```

Similarly, after moving right, the next move must be left.



# State Transition

If we move to the **left child**:

```python
traverse(current_node.left, 0, left_count + 1)
```

The new state is:

```text
left_count = 0

right_count = left_count + 1
```

because after moving left, the next direction must be right.

If we move to the **right child**:

```python
traverse(current_node.right, right_count + 1, 0)
```

The new state is:

```text
left_count = right_count + 1

right_count = 0
```

because after moving right, the next direction must be left.



# Why Do We Reset One Count to `0`?

Consider:

```text
Left → Left
```

This is not a valid ZigZag because the direction did not change.

After making a left move, the next move must be right.

Therefore:

```text
Left move

↓

left_count = 0

right_count = previous left_count + 1
```

Similarly:

```text
Right move

↓

right_count = 0

left_count = previous right_count + 1
```



# Intuition

At every node:

```text
Check the current ZigZag length

↓

Try moving left

↓

Try moving right

↓

Update the maximum
```

When moving left:

```text
Previous left path
        ↓
Add 1
        ↓
Become right path
```

When moving right:

```text
Previous right path
        ↓
Add 1
        ↓
Become left path
```



# Algorithm

1. Initialize:

```python
max_length = 0
```

2. Start DFS from the root:

```python
traverse(root, 0, 0)
```

3. At every node, update the maximum:

```python
max_length = max(max_length, left_count, right_count)
```

4. If the left child exists:

```python
traverse(
    current_node.left,
    0,
    left_count + 1
)
```

5. If the right child exists:

```python
traverse(
    current_node.right,
    right_count + 1,
    0
)
```

6. After traversing the entire tree, return:

```python
max_length
```



# Code

```python
class Solution(object):

    def longestZigZag(self, root):

        max_length = 0

        def traverse(current_node, left_count, right_count):

            nonlocal max_length

            max_length = max(max_length, left_count, right_count)

            if current_node.left is not None:
                traverse(
                    current_node.left,
                    0,
                    left_count + 1
                )

            if current_node.right is not None:
                traverse(
                    current_node.right,
                    right_count + 1,
                    0
                )

        traverse(root, 0, 0)

        return max_length
```



# Walkthrough

Consider:

```text
        1
       / \
      2   3
       \
        4
       /
      5
```

The ZigZag path is:

```text
1 → 2 → 4 → 5
```

Directions:

```text
Left → Right → Left
```

Therefore:

```text
ZigZag Length = 3
```



## Start at Node 1

Initially:

```text
left_count = 0

right_count = 0

max_length = 0
```



## Move Left

We move:

```text
1 → 2
```

This is one edge.

The next direction must be right.

Therefore:

```text
left_count = 0

right_count = 1
```

The maximum becomes:

```text
max_length = 1
```



## Move Right

From node `2`:

```text
2 → 4
```

This is another alternating move.

Therefore:

```text
left_count = right_count + 1

left_count = 2
```

The state becomes:

```text
left_count = 2

right_count = 0
```

The maximum becomes:

```text
max_length = 2
```



## Move Left Again

From node `4`:

```text
4 → 5
```

Again the direction alternates.

Therefore:

```text
right_count = left_count + 1

right_count = 3
```

Now:

```text
max_length = 3
```

The final path is:

```text
1 → 2 → 4 → 5
```

with:

```text
Left → Right → Left
```

So the answer is:

```text
3
```



# Dry Run

| Node | `left_count` | `right_count` | `max_length` |
| ---- | ------------ | ------------- | ------------ |
| 1    | 0            | 0             | 0            |
| 2    | 0            | 1             | 1            |
| 4    | 2            | 0             | 2            |
| 5    | 0            | 3             | 3            |

Final answer:

```text
3
```



# Why Does This Work?

Every node can be reached through a ZigZag path.

Instead of restarting the entire search from every node, we carry the current path information during DFS.

For each node, we know:

```text
How long is the ZigZag path if the next direction is left?

How long is the ZigZag path if the next direction is right?
```

Then we continue the path by switching the direction.

This allows every node to be processed once.



# Why Do We Track `max_length`?

The longest ZigZag path can end at any node.

For example:

```text
        1
       /
      2
       \
        3
         \
          4
```

The path:

```text
1 → 2 → 3
```

is a valid ZigZag:

```text
Left → Right
```

but:

```text
3 → 4
```

continues in the same direction and therefore cannot extend the ZigZag.

So while traversing, we update:

```python
max_length = max(max_length, left_count, right_count)
```

at every node.



# Complexity

```text
Time : O(n)
```

Every node is visited exactly once.

```text
Space : O(h)
```

The recursion stack depends on the height of the tree.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```



# Common Mistakes

### ❌ Counting Nodes Instead of Edges

The problem asks for the number of **edges**.

For:

```text
1 → 2 → 3
```

there are:

```text
3 nodes
```

but:

```text
2 edges
```

Therefore:

```text
ZigZag Length = 2
```



### ❌ Not Resetting the Direction

After moving left:

```text
Left
```

the next move must be:

```text
Right
```

So:

```python
traverse(current_node.left, 0, left_count + 1)
```

The left count is reset to `0`.



### ❌ Forgetting to Add 1

When moving from one node to another, we have travelled one additional edge.

Therefore:

```python
left_count + 1
```

or:

```python
right_count + 1
```

is required.



### ❌ Only Starting From the Root

The longest ZigZag path can start at **any node**.

The DFS naturally considers every node as it traverses the tree.



### ❌ Confusing Direction With Child Value

The problem is not about whether node values are increasing or decreasing.

It is only about alternating:

```text
Left → Right → Left → Right
```

or:

```text
Right → Left → Right → Left
```



# Similar Problems

- Binary Tree Maximum Depth
- Diameter of Binary Tree
- Longest Univalue Path
- Path Sum III
- Count Good Nodes in Binary Tree



# Interview Takeaway

## Recognition

```text
Binary Tree

DFS

Recursion

State Tracking

Longest Path
```

## Core Trick

```text
At Every Node

↓

Track Left Count

↓

Track Right Count

↓

If Moving Left:

    Left Count = 0
    Right Count = Left Count + 1

↓

If Moving Right:

    Right Count = 0
    Left Count = Right Count + 1

↓

Update Global Maximum

↓

Continue DFS

↓

Return Maximum ZigZag Length
``` 

