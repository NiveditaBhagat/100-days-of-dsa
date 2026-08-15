
# Maximum Depth of Binary Tree (LeetCode 104)

Given the `root` of a binary tree, return its **maximum depth**.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The longest path is:

```text
3 → 20 → 15
```

Therefore:

```text
Maximum Depth = 3
```



## Example 1

```text
Input:

root = [3,9,20,null,null,15,7]

Output:

3
```

Explanation

```text
        3
       / \
      9   20
         /  \
        15   7
```

The longest path contains:

```text
3 → 20 → 15
```

So the maximum depth is:

```text
3
```



## Example 2

```text
Input:

root = [1,null,2]

Output:

2
```

Explanation

```text
    1
     \
      2
```

The longest path is:

```text
1 → 2
```

Therefore:

```text
Maximum Depth = 2
```



## Example 3

```text
Input:

root = []

Output:

0
```

Explanation

```text
The tree is empty.

Return 0.
```



## Constraints

```text
0 <= Number of Nodes <= 10^4

-100 <= Node.val <= 100
```



# Pattern

```text
Binary Tree

Depth First Search

Recursion

Tree Traversal
```



# Recognition

Use this pattern when the problem involves:

- Finding the maximum depth of a binary tree
- Finding the height of a tree
- Finding the longest root-to-leaf path
- Recursively exploring left and right subtrees
- Comparing results from two child subtrees



# Brute Force

## Intuition

We can traverse the tree and keep track of the current depth.

At every node, we increase the depth by `1`.

Then recursively explore the left and right subtrees.

At the end, return the larger depth.



## Algorithm

1. If the current node is `None`, return `0`.
2. Increase the current depth by `1`.
3. Store the current depth for both left and right sides.
4. If the left child exists, recursively calculate its depth.
5. If the right child exists, recursively calculate its depth.
6. Return the maximum of the left and right depths.



# Optimal Approach (Recursive DFS with Depth Tracking)

## Key Observation

Instead of maintaining a global maximum,

we pass the current depth into the recursive function.

For every node:

```python
depth += 1
```

Then we explore both children.

The recursive call returns the maximum depth found in that subtree.



# Why Do We Pass `depth`?

Suppose we have:

```text
        3
       /
      9
     /
    5
```

When we start:

```text
depth = 0
```

At node `3`:

```text
depth = 1
```

At node `9`:

```text
depth = 2
```

At node `5`:

```text
depth = 3
```

Therefore, when we reach the deepest node, the `depth` variable represents how many nodes we have visited along that path.



# Intuition

At every node:

```text
Increase depth

↓

Start with current depth for left and right

↓

Explore left subtree if it exists

↓

Explore right subtree if it exists

↓

Return the larger depth
```

The important part is that each recursive call receives the current depth:

```python
traverse(current_node.left, depth)
```

and

```python
traverse(current_node.right, depth)
```



# Why Do We Use `left_depth` and `right_depth`?

At each node, we need to know which side has the longer path.

So we initialize:

```python
left_depth = depth

right_depth = depth
```

This also handles the case where a child does not exist.

If the left child exists:

```python
left_depth = traverse(current_node.left, depth)
```

If the right child exists:

```python
right_depth = traverse(current_node.right, depth)
```

Finally:

```python
return max(left_depth, right_depth)
```



# Algorithm

1. If `root` is `None`, return:

```text
0
```

2. Define a recursive function:

```python
traverse(current_node, depth)
```

3. Increase the depth:

```python
depth += 1
```

4. Initialize:

```python
left_depth = depth
right_depth = depth
```

5. If the left child exists:

```python
left_depth = traverse(current_node.left, depth)
```

6. If the right child exists:

```python
right_depth = traverse(current_node.right, depth)
```

7. Return:

```python
max(left_depth, right_depth)
```

8. Start the traversal with:

```python
traverse(root, 0)
```



# Code

```python
class Solution(object):

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0

        def traverse(current_node, depth):

            depth += 1

            left_depth = depth
            right_depth = depth

            if current_node.left is not None:
                left_depth = traverse(current_node.left, depth)

            if current_node.right is not None:
                right_depth = traverse(current_node.right, depth)

            return max(left_depth, right_depth)

        return traverse(root, 0)
```



# Walkthrough

## Example

```text
root = [3,9,20,null,null,15,7]
```

Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Start:

```text
traverse(3, 0)
```



## At Node 3

Increase depth:

```text
depth = 1
```

Initialize:

```text
left_depth = 1
right_depth = 1
```

Node `3` has both children.

So we recursively explore:

```text
traverse(9, 1)

traverse(20, 1)
```



## At Node 9

Increase depth:

```text
depth = 2
```

Node `9` has no children.

Therefore:

```text
left_depth = 2

right_depth = 2
```

Return:

```text
max(2,2) = 2
```

So:

```text
left_depth = 2
```

for node `3`.



## At Node 20

Increase depth:

```text
depth = 2
```

Node `20` has:

```text
left = 15

right = 7
```

So we call:

```text
traverse(15, 2)

traverse(7, 2)
```



## At Node 15

Increase:

```text
depth = 3
```

No children.

Return:

```text
3
```



## At Node 7

Increase:

```text
depth = 3
```

No children.

Return:

```text
3
```



## Back at Node 20

We now have:

```text
left_depth = 3

right_depth = 3
```

Return:

```text
max(3,3) = 3
```

So for node `3`:

```text
right_depth = 3
```



## Back at Node 3

We have:

```text
left_depth = 2

right_depth = 3
```

Therefore:

```text
max(2,3) = 3
```

Return:

```text
3
```

Final answer:

```text
3
```



# Dry Run

| Current Node | Incoming Depth | New Depth | Left Depth | Right Depth | Returned |
|--------------|----------------|-----------|------------|-------------|----------|
| 9 | 1 | 2 | 2 | 2 | 2 |
| 15 | 2 | 3 | 3 | 3 | 3 |
| 7 | 2 | 3 | 3 | 3 | 3 |
| 20 | 1 | 2 | 3 | 3 | 3 |
| 3 | 0 | 1 | 2 | 3 | 3 |



# Understanding the Recursion

The traversal goes down the tree while increasing `depth`.

```text
3
↓
20
↓
15
```

Depth becomes:

```text
0
↓
1
↓
2
↓
3
```

When recursion returns,

the deepest value travels back upward.

For example:

```text
traverse(15, 2)

↓

depth = 3

↓

return 3
```

Then node `20` receives:

```text
left_depth = 3
```

and compares it with the right subtree.

Finally, node `3` compares:

```text
left_depth = 2

right_depth = 3
```

and returns:

```text
3
```



# Why Don't We Need `nonlocal`?

We don't need:

```python
nonlocal max_depth
```

because we are not maintaining one shared variable.

Instead, every recursive call returns its answer:

```python
return max(left_depth, right_depth)
```

For example:

```text
Node 15 → returns 3

Node 7  → returns 3

Node 20 → receives 3 and 3 → returns 3

Node 9  → returns 2

Node 3  → receives 2 and 3 → returns 3
```

The answer naturally travels back through the recursion.



# Why Do We Initialize Both Depths to `depth`?

We use:

```python
left_depth = depth
right_depth = depth
```

before checking the children.

Suppose we have:

```text
    1
     \
      2
```

At node `1`:

```text
depth = 1
```

There is no left child.

Therefore:

```text
left_depth = 1
```

The right child exists, so:

```text
right_depth = traverse(2, 1)
```

which returns:

```text
2
```

Finally:

```text
max(1,2) = 2
```

This allows the same logic to work when one or both children are missing.



# Complexity

```text
Time : O(n)
```

Every node is visited exactly once.

```text
Space : O(h)
```

The recursive call stack depends on the height of the tree.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```



# Common Mistakes

### ❌ Forgetting to increase depth

Wrong:

```python
def traverse(current_node, depth):

    left_depth = depth
    right_depth = depth
```

The current node must be counted.

Correct:

```python
depth += 1
```



### ❌ Starting with depth 1

Wrong:

```python
return traverse(root, 1)
```

Your traversal increases depth when it reaches a node.

Therefore start with:

```python
return traverse(root, 0)
```

Then the root becomes:

```text
depth = 1
```



### ❌ Returning `depth + 1` at the end

The depth has already been increased:

```python
depth += 1
```

So the return should simply be:

```python
return max(left_depth, right_depth)
```



### ❌ Only Traversing One Side

Wrong:

```python
if current_node.left is not None:
    left_depth = traverse(current_node.left, depth)
```

The longest path could be on the right.

Always check both:

```python
if current_node.left is not None:
    left_depth = traverse(current_node.left, depth)

if current_node.right is not None:
    right_depth = traverse(current_node.right, depth)
```



### ❌ Forgetting the Base Case

Wrong:

```python
def maxDepth(self, root):

    def traverse(current_node, depth):
        ...
```

You need to handle an empty tree:

```python
if root is None:
    return 0
```



### ❌ Using `nonlocal` Unnecessarily

You don't need:

```python
nonlocal max_depth
```

because your recursive function returns the maximum depth of each subtree.



# Similar Problems

- Minimum Depth of Binary Tree
- Diameter of Binary Tree
- Balanced Binary Tree
- Same Tree
- Invert Binary Tree



# Interview Takeaway

## Recognition

```text
Binary Tree

DFS

Recursion

Depth Tracking

Compare Left and Right Subtrees
```

## Core Trick

```text
Start Depth at 0

↓

Visit Current Node

↓

depth += 1

↓

Explore Left Subtree

↓

Explore Right Subtree

↓

Take max(left_depth, right_depth)

↓

Return Maximum Depth
```

