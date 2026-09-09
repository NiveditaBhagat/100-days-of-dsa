# Binary Tree Right Side View (LeetCode 199)

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it.

Return the values of the nodes that are visible from the right side, ordered from top to bottom.

For each level of the tree, the **rightmost node** is visible.

For example:

```text
        1
       / \
      2   3
       \   \
        5   4
```

The right side view is:

```text
1 → 3 → 4
```



## Example 1

```text
Input:

root = [1,2,3,null,5,null,4]

Output:

[1,3,4]
```

Explanation

```text
        1
       / \
      2   3
       \   \
        5   4
```

Visible nodes from the right side:

```text
1
3
4
```

Therefore:

```text
[1,3,4]
```



## Example 2

```text
Input:

root = [1,2,3,4,null,null,null,5]

Output:

[1,3,4,5]
```

Explanation

```text
        1
       / \
      2   3
     /
    4
   /
  5
```

The rightmost visible node at each level is:

```text
1
3
4
5
```



## Example 3

```text
Input:

root = [1,null,3]

Output:

[1,3]
```

Explanation

```text
1
 \
  3
```

Both nodes are visible from the right side.



## Example 4

```text
Input:

root = []

Output:

[]
```

Explanation

```text
The tree is empty.

Return [].
```



## Constraints

```text
0 <= Number of Nodes <= 100

-100 <= Node.val <= 100
```



# Pattern

```text
Binary Tree

Breadth First Search (BFS)

Level Order Traversal

Queue
```



# Recognition

Use this pattern when the problem asks:

- Process a binary tree level by level
- Find the first or last node at each level
- Find the leftmost or rightmost node
- Return information about each tree level
- Find the visible nodes from one side of a tree



# Brute Force

## Intuition

One approach is to traverse the tree in a way that prioritizes the right side and keep track of the first node encountered at each depth.

However, the problem naturally maps to **level-order traversal**, because we need exactly one node from every level.



# Optimal Approach (BFS / Level Order Traversal)

## Key Observation

At every level, we only need the **last node processed**.

For example:

```text
        1
       / \
      2   3
       \   \
        5   4
```

Level 1:

```text
1
```

Level 2:

```text
2 → 3
```

The last node is:

```text
3
```

Level 3:

```text
5 → 4
```

The last node is:

```text
4
```

Therefore:

```text
[1,3,4]
```



# Why Do We Use a Queue?

BFS processes the tree **level by level**.

The queue contains the nodes that need to be processed.

Initially:

```text
queue = [1]
```

After processing node `1`:

```text
queue = [2,3]
```

After processing level 2:

```text
queue = [5,4]
```

So the queue naturally allows us to process one complete level at a time.



# Why Do We Need `level_size`?

At the beginning of each level:

```python
level_size = len(queue)
```

This tells us exactly how many nodes belong to the current level.

For example:

```text
queue = [2,3,5,4]
```

If only:

```text
2,3
```

belong to the current level, then:

```text
level_size = 2
```

We process exactly two nodes.

The nodes added during this process:

```text
5,4
```

belong to the **next level**.



# Algorithm

1. If `root` is `None`, return:

```text
[]
```

2. Create an empty result list:

```python
result = []
```

3. Initialize the queue with the root:

```python
queue = [root]
```

4. While the queue is not empty:

   - Store the number of nodes in the current level.

   ```python
   level_size = len(queue)
   ```

   - Process exactly `level_size` nodes.

   - Remove each node from the queue.

   - If it is the last node of the current level, add its value to `result`.

   - Add its left and right children to the queue.

5. Return `result`.



# Code

```python
class Solution(object):

    def rightSideView(self, root):

        if root is None:
            return []

        result = []
        queue = [root]

        while queue:

            level_size = len(queue)

            for i in range(level_size):

                current_node = queue.pop(0)

                if i == level_size - 1:
                    result.append(current_node.val)

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

        return result
```



# Walkthrough

## Example

```text
root = [1,2,3,null,5,null,4]
```

Tree:

```text
        1
       / \
      2   3
       \   \
        5   4
```

Initially:

```text
queue = [1]

result = []
```



## Level 1

Queue:

```text
[1]
```

Therefore:

```text
level_size = 1
```

Process node:

```text
1
```

Since:

```text
i = 0

level_size - 1 = 0
```

this is the last node of the level.

Add:

```text
result = [1]
```

Add its children:

```text
queue = [2,3]
```



## Level 2

Queue:

```text
[2,3]
```

Therefore:

```text
level_size = 2
```

### Process node 2

```text
i = 0
```

It is not the last node because:

```text
level_size - 1 = 1
```

Add its child:

```text
5
```

Queue becomes:

```text
[3,5]
```



### Process node 3

```text
i = 1
```

Now:

```text
i == level_size - 1
```

So node `3` is the rightmost node of this level.

Add:

```text
result = [1,3]
```

Add its child:

```text
4
```

Queue becomes:

```text
[5,4]
```



## Level 3

Queue:

```text
[5,4]
```

Therefore:

```text
level_size = 2
```

### Process node 5

```text
i = 0
```

Not the last node.



### Process node 4

```text
i = 1
```

This is the last node of the level.

Add:

```text
result = [1,3,4]
```



## Final Result

The queue is now empty.

Return:

```text
[1,3,4]
```


# Dry Run

| Level | Nodes Processed | Rightmost Node | Result |
|------:|-----------------|----------------|--------|
| 1 | 1 | 1 | [1] |
| 2 | 2 → 3 | 3 | [1,3] |
| 3 | 5 → 4 | 4 | [1,3,4] |



# Why `i == level_size - 1`?

Suppose the current level has:

```text
[2,3]
```

Then:

```text
level_size = 2
```

The indices are:

```text
2 → i = 0
3 → i = 1
```

The last index is:

```text
level_size - 1
```

which is:

```text
2 - 1 = 1
```

Therefore:

```python
if i == level_size - 1:
```

means:

```text
If this is the last node of the current level,
add it to the result.
```



# Why Do We Add Children After Checking the Rightmost Node?

The rightmost node is determined using the nodes that already belong to the current level.

So we first check:

```python
if i == level_size - 1:
    result.append(current_node.val)
```

Then we add children:

```python
if current_node.left is not None:
    queue.append(current_node.left)

if current_node.right is not None:
    queue.append(current_node.right)
```

Those children belong to the **next level**.



# Important Detail About the Queue

The solution uses:

```python
queue.pop(0)
```

to remove the first element.

Conceptually, this is a queue:

```text
First In → First Out
```

For example:

```text
[2,3,5,4]

pop(0)

↓

3,5,4
```

The first node inserted is processed first.



# Complexity

The intended BFS traversal visits every node once.

```text
Time : O(n)
```

However, in Python, using:

```python
queue.pop(0)
```

takes `O(n)` because all remaining elements may need to be shifted.

Therefore, with this **exact implementation**, the worst-case time can be:

```text
O(n²)
```

The standard optimized Python implementation would use `collections.deque` with:

```python
popleft()
```

which makes removing the first element `O(1)`.

Then the complexity becomes:

```text
Time : O(n)

Space : O(n)
```

For this solution, the extra space is:

```text
O(n)
```

because the queue can contain many nodes from a level.


# Common Mistakes

### ❌ Taking the last node of the entire queue

We need the last node of the **current level**, not the entire queue.

That's why we save:

```python
level_size = len(queue)
```

before processing the level.



### ❌ Using `i == len(queue) - 1`

The queue changes while processing the level because children are added.

Therefore, using the changing queue length can give incorrect results.

Use:

```python
level_size = len(queue)
```

and then:

```python
if i == level_size - 1:
```



### ❌ Only Traversing the Right Child

Wrong:

```python
current_node.right
```

The visible node might come from the left subtree.

For example:

```text
    1
   /
  2
   \
    3
```

The right side view is:

```text
[1,2,3]
```

So both children must be added to the queue.



### ❌ Thinking Right Side View Means Right Subtree Only

The right side view does **not** mean:

```text
Only traverse right children.
```

It means:

```text
For every level,

take the rightmost node.
```



# Similar Problems

- Binary Tree Level Order Traversal
- Binary Tree Left Side View
- Average of Levels in Binary Tree
- Maximum Level Sum of a Binary Tree
- Find Bottom Left Tree Value



# Interview Takeaway

## Recognition

```text
Binary Tree

BFS

Level Order Traversal

Queue

Rightmost Node of Each Level
```

## Core Trick

```text
Process Tree Level by Level

↓

Store level_size

↓

Process Exactly One Level

↓

Identify Last Node Using

i == level_size - 1

↓

Add That Node to Result

↓

Move to Next Level
```
