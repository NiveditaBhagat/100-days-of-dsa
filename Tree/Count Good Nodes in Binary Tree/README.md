
# Count Good Nodes in Binary Tree (LeetCode 1448)

You are given the **root** of a binary tree.

A node `X` is called **good** if there are no nodes with a value greater than `X` on the path from the root to `X`.

Return the number of **good nodes** in the binary tree.

For example:

```text
        3
       / \
      1   4
     /   / \
    3   1   5
```

The good nodes are:

```text
3 → Root

4 → 3 → 4

3 → 3 → 1 → 3

5 → 3 → 4 → 5
```

Therefore:

```text
Answer = 4
```



## Example 1

```text
Input:

root = [3,1,4,3,null,1,5]

Output:

4
```

Explanation:

```text
        3
       / \
      1   4
     /   / \
    3   1   5
```

Check each relevant path:

```text
Node 3:
3

3 is the maximum → Good


Node 1:
3 → 1

3 > 1 → Not Good


Node 4:
3 → 4

4 is the maximum → Good


Node 3:
3 → 1 → 3

3 is the maximum → Good


Node 1:
3 → 4 → 1

4 > 1 → Not Good


Node 5:
3 → 4 → 5

5 is the maximum → Good
```

Good nodes:

```text
3, 4, 3, 5
```

Therefore:

```text
Answer = 4
```



## Example 2

```text
Input:

root = [3,3,null,4,2]

Output:

3
```

Explanation:

```text
        3
       /
      3
     / \
    4   2
```

The paths are:

```text
3

3 → 3

3 → 3 → 4

3 → 3 → 2
```

Good nodes:

```text
3
3
4
```

Node `2` is not good because:

```text
3 > 2
```

Therefore:

```text
Answer = 3
```



## Example 3

```text
Input:

root = [1]

Output:

1
```

Explanation:

```text
1
```

The root is always good because there are no nodes before it.

Therefore:

```text
Answer = 1
```



## Constraints

```text
1 <= Number of Nodes <= 10^5

-10^4 <= Node.val <= 10^4
```



# Pattern

```text
Binary Tree

DFS

Recursion

Path Tracking

Maximum Value Along Path
```



# Recognition

Use this pattern when the problem asks whether a node depends on values seen on the path from the root.

Look for phrases such as:

- Path from root to node
- Maximum value seen so far
- Minimum value seen so far
- Count nodes satisfying a path condition
- Track information while traversing a tree



# Brute Force

## Intuition

For every node, we could find the complete path from the root to that node and check whether any previous node has a greater value.

This would require repeatedly examining paths.



## Complexity

In the worst case, repeatedly checking paths can take:

```text
Time : O(n²)
```

for a skewed tree.

We can do better by carrying the maximum value seen so far during DFS.



# Optimal Approach (DFS With Maximum Seen)

## Key Observation

While traversing from the root to a node, we only need one piece of information:

```text
Maximum value seen on the current path
```

Suppose we have:

```text
        3
       /
      1
     /
    3
```

When we reach the last `3`, the path is:

```text
3 → 1 → 3
```

The maximum value seen before reaching this node is:

```text
3
```

Since:

```text
3 >= 3
```

the node is good.



# What Does `max_seen` Mean?

In the recursive function:

```python
traverse(current_node, max_seen)
```

`max_seen` represents:

```text
The maximum node value encountered
from the root up to the current node's parent.
```

For example:

```text
3 → 1 → 4
```

When processing node `4`:

```text
max_seen = 3
```

Since:

```text
4 >= 3
```

node `4` is good.

Then we update:

```python
max_seen = 4
```

because `4` is now the largest value on the path.



# Intuition

At every node:

```text
Compare current node with max_seen

↓

If current node >= max_seen

    Node is good

↓

Update max_seen if necessary

↓

Traverse left subtree

↓

Traverse right subtree

↓

Add the counts returned by both subtrees
```

The important part is that every recursive call receives the maximum value seen along its own path.



# Why Do We Pass `max_seen`?

Consider:

```text
        3
       /
      1
     /
    2
```

When we reach `2`, we need to remember:

```text
3 → 1 → 2
```

The maximum value seen is:

```text
3
```

Since:

```text
2 < 3
```

node `2` is not good.

We don't need to store the entire path.

We only need:

```text
max_seen = 3
```

This makes the solution efficient.



# Why Do We Initialize `max_seen` With `root.val`?

The root is always a good node.

We start with:

```python
traverse(root, root.val)
```

At the root:

```python
current_node.val >= max_seen
```

becomes:

```text
root.val >= root.val
```

which is true.

Therefore:

```text
count = 1
```

and the root is correctly counted as good.



# Algorithm

1. If the root is `None`, return `0`.

2. Start DFS with:

```python
traverse(root, root.val)
```

3. At every node, compare:

```python
current_node.val >= max_seen
```

4. If true:

```python
count = 1
```

and update:

```python
max_seen = current_node.val
```

5. Otherwise:

```python
count = 0
```

6. Recursively traverse the left subtree.

7. Recursively traverse the right subtree.

8. Add both returned counts to the current count.

9. Return the total count.



# Code

```python
class Solution(object):

    def goodNodes(self, root):

        if root is None:
            return 0

        def traverse(current_node, max_seen):

            if current_node.val >= max_seen:
                count = 1
                max_seen = current_node.val
            else:
                count = 0

            if current_node.left is not None:
                count += traverse(current_node.left, max_seen)

            if current_node.right is not None:
                count += traverse(current_node.right, max_seen)

            return count

        return traverse(root, root.val)
```



# Walkthrough

## Example

```text
root = [3,1,4,3,null,1,5]
```

Tree:

```text
        3
       / \
      1   4
     /   / \
    3   1   5
```

We start with:

```text
current_node = 3

max_seen = 3
```



## Node 3

Check:

```text
3 >= 3
```

True.

Therefore:

```text
count = 1
```

The root is good.

`max_seen` remains:

```text
3
```

Now traverse both children.



## Node 1

Path:

```text
3 → 1
```

Current maximum:

```text
max_seen = 3
```

Check:

```text
1 >= 3
```

False.

Therefore:

```text
count = 0
```

`max_seen` remains:

```text
3
```



## Node 3

Path:

```text
3 → 1 → 3
```

Check:

```text
3 >= 3
```

True.

Therefore:

```text
count = 1
```

This node is good.



## Node 4

Path:

```text
3 → 4
```

Check:

```text
4 >= 3
```

True.

Therefore:

```text
count = 1
```

Update:

```text
max_seen = 4
```



## Node 1

Path:

```text
3 → 4 → 1
```

Current maximum:

```text
4
```

Check:

```text
1 >= 4
```

False.

Therefore:

```text
count = 0
```



## Node 5

Path:

```text
3 → 4 → 5
```

Current maximum:

```text
4
```

Check:

```text
5 >= 4
```

True.

Therefore:

```text
count = 1
```

Update:

```text
max_seen = 5
```


# Count Flow

The recursive calls return counts upward.

For the left subtree:

```text
Node 1
    |
    └── Node 3

Count = 0 + 1 = 1
```

For the right subtree:

```text
Node 4
   / \
  1   5

Count = 1 + 0 + 1 = 2
```

Finally, the root contributes:

```text
1
```

Total:

```text
1 + 1 + 2 = 4
```

Therefore:

```text
Answer = 4
```



# Dry Run

| Node | `max_seen` Before | Good? | `max_seen` After | Count |
|------|-------------------|-------|------------------|-------|
| 3 | 3 | Yes | 3 | 1 |
| 1 | 3 | No | 3 | 0 |
| 3 | 3 | Yes | 3 | 1 |
| 4 | 3 | Yes | 4 | 1 |
| 1 | 4 | No | 4 | 0 |
| 5 | 4 | Yes | 5 | 1 |

Total:

```text
1 + 0 + 1 + 1 + 0 + 1 = 4
```



# How the Count Works

This is an important part of the solution.

At every node:

```python
count = 1
```

if the node is good.

Otherwise:

```python
count = 0
```

Then we add the counts from the children:

```python
count += traverse(current_node.left, max_seen)

count += traverse(current_node.right, max_seen)
```

For example:

```text
        3
       /
      1
     /
    3
```

At node `3`:

```text
count = 1
```

At node `1`:

```text
count = 0
```

At the last node `3`:

```text
count = 1
```

The recursive result becomes:

```text
1 + 0 + 1 = 2
```

So the count is naturally passed back up through the recursion.



# Why We Update `max_seen`

Suppose:

```text
3 → 4 → 5
```

At node `4`:

```text
4 >= 3
```

so `4` is good.

We must now update:

```text
max_seen = 4
```

When we reach `5`:

```text
5 >= 4
```

so `5` is also good.

If we didn't update `max_seen`, we would incorrectly compare `5` only against `3`.



# Why `>=` and Not `>`

A node is good when there is **no node greater than it** on the path.

Equal values are allowed.

For example:

```text
3 → 3
```

The second `3` is good because there is no value **greater than 3**.

Therefore:

```python
current_node.val >= max_seen
```

is correct.

Not:

```python
current_node.val > max_seen
```



# Complexity

```text
Time : O(n)
```

Every node is visited exactly once.

```text
Space : O(h)
```

The recursive call stack can contain up to `h` nodes, where `h` is the height of the tree.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```


# Common Mistakes

### ❌ Comparing Only With the Parent

Wrong idea:

```text
Compare current node only with parent
```

A node can be smaller than its parent but still be greater than every node before it.

We need the maximum value from the **entire path**.



### ❌ Using `>` Instead of `>=`

Wrong:

```python
if current_node.val > max_seen:
```

This would incorrectly mark equal values as not good.

Correct:

```python
if current_node.val >= max_seen:
```



### ❌ Forgetting to Update `max_seen`

Wrong:

```python
if current_node.val >= max_seen:
    count = 1
```

We also need:

```python
max_seen = current_node.val
```

Otherwise descendants won't know that the current node became the new maximum.



### ❌ Resetting `max_seen` for Every Node

`max_seen` must represent the maximum value along the current root-to-node path.

It should be passed into recursive calls:

```python
traverse(current_node.left, max_seen)

traverse(current_node.right, max_seen)
```



### ❌ Forgetting to Add Child Counts

The current node's count is not enough.

We need:

```python
count += traverse(current_node.left, max_seen)

count += traverse(current_node.right, max_seen)
```

This allows the total number of good nodes to propagate back to the root.



# Similar Problems

- Path Sum
- Binary Tree Maximum Path Sum
- Maximum Depth of Binary Tree
- Diameter of Binary Tree
- Path Sum II



# Interview Takeaway

## Recognition

```text
Binary Tree

DFS

Recursion

Path Tracking

Maximum Value Along Path
```

## Core Trick

```text
Pass Maximum Value Seen So Far

↓

Compare Current Node With max_seen

↓

If Current Node >= max_seen

    Count It

↓

Update max_seen

↓

Traverse Left

↓

Traverse Right

↓

Add All Counts

↓

Return Total Good Nodes
```

