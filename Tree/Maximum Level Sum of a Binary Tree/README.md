# Maximum Level Sum of a Binary Tree (LeetCode 1161)

You are given the `root` of a binary tree.

The level of the root node is:

```text
Level 1
```

Its children are:

```text
Level 2
```

Their children are:

```text
Level 3
```

and so on.

Return the **smallest level** whose sum of node values is maximal.



## Example 1

```text
Input:

root = [1,7,0,7,-8,null,null]

Output:

2
```

Tree:

```text
        1
       / \
      7   0
     / \
    7  -8
```

Level sums:

```text
Level 1 = 1

Level 2 = 7 + 0 = 7

Level 3 = 7 + (-8) = -1
```

The maximum sum is:

```text
7
```

which occurs at:

```text
Level 2
```

Therefore:

```text
Answer = 2
```



## Example 2

```text
Input:

root = [989,null,10250,98693,-89388,null,null,null,-32127]

Output:

2
```



## Constraints

```text
1 <= Number of Nodes <= 10^4

-10^5 <= Node.val <= 10^5
```



# Pattern

```text
Binary Tree

Breadth First Search (BFS)

Level Order Traversal

Queue
```



# Recognition

Use this pattern when the problem asks you to:

- Process a binary tree level by level
- Calculate something for every level
- Find the maximum/minimum value for a level
- Calculate the sum of nodes at each level
- Return a specific level based on its values



# Brute Force

## Intuition

We could traverse the tree multiple times.

For each level:

1. Find all nodes belonging to that level.
2. Calculate their sum.
3. Compare it with the maximum sum.

However, repeatedly traversing the tree is unnecessary.

We can calculate each level's sum during a single level-order traversal.



## Complexity

```text
Time : O(n)
```

```text
Space : O(n)
```



# Optimal Approach (BFS / Level Order Traversal)

## Key Observation

A binary tree can be processed one level at a time using a queue.

For example:

```text
        1
       / \
      7   0
     / \
    7  -8
```

The queue initially contains:

```text
[1]
```

After processing level 1:

```text
[7, 0]
```

After processing level 2:

```text
[7, -8]
```

Therefore, the queue naturally gives us all nodes of the next level.



# Why Do We Need `level_size`?

At the beginning of every level:

```python
level_size = len(queue)
```

This tells us exactly how many nodes belong to the current level.

For example:

```text
Queue:

[7, 0, 5, 8]
```

If these four nodes belong to the current level:

```text
level_size = 4
```

We process exactly four nodes.

While processing them, their children are added to the queue.

Those children belong to the **next level**, not the current level.

Therefore:

```python
for _ in range(level_size):
```

allows us to process one complete level at a time.



# Intuition

At every level:

```text
Get number of nodes in current level

↓

Process exactly those nodes

↓

Calculate their sum

↓

Add their children to queue

↓

Compare current level sum with maximum sum

↓

Move to next level
```



# Variables

We use:

```python
queue
level
max_sum
answer
```



## `queue`

Stores the nodes that need to be processed.

Initially:

```python
queue = [root]
```



## `level`

Keeps track of the current level number.

Initially:

```python
level = 1
```



## `max_sum`

Stores the largest level sum found so far.

Initially:

```python
max_sum = root.val
```

We start with the root's value because the root is level 1.

---

## `answer`

Stores the level having the maximum sum.

Initially:

```python
answer = 1
```


# Algorithm

1. Put the root into the queue.

```python
queue = [root]
```

2. Start from level 1.

```python
level = 1
```

3. Initialize the maximum sum using the root.

```python
max_sum = root.val
```

4. Set the initial answer to level 1.

```python
answer = 1
```

5. While the queue is not empty:

   - Get the number of nodes in the current level.

   ```python
   len_size = len(queue)
   ```

   - Initialize the current level sum.

   ```python
   level_sum = 0
   ```

   - Process exactly `len_size` nodes.

   - Add each node's value to `level_sum`.

   - Add its left and right children to the queue.

6. After processing the complete level:

```python
if level_sum > max_sum:
```

update:

```python
max_sum = level_sum
answer = level
```

7. Move to the next level.

```python
level += 1
```

8. Return:

```python
answer
```



# Code

```python
class Solution(object):

    def maxLevelSum(self, root):

        queue = [root]
        level = 1
        max_sum = root.val
        answer = 1

        while queue:

            len_size = len(queue)
            level_sum = 0

            for _ in range(len_size):

                curr_node = queue.pop(0)

                level_sum += curr_node.val

                if curr_node.left is not None:
                    queue.append(curr_node.left)

                if curr_node.right is not None:
                    queue.append(curr_node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer = level

            level += 1

        return answer
```



# Walkthrough

## Example

```text
root = [1,7,0,7,-8,null,null]
```

Tree:

```text
        1
       / \
      7   0
     / \
    7  -8
```



## Initial State

```text
queue = [1]

level = 1

max_sum = 1

answer = 1
```



## Level 1

At the beginning:

```text
queue = [1]
```

Therefore:

```text
len_size = 1
```

Process one node:

```text
1
```

Calculate:

```text
level_sum = 1
```

Add its children:

```text
queue = [7, 0]
```

Compare:

```text
level_sum = 1
max_sum = 1
```

Since:

```text
1 > 1
```

is false, we do not update the answer.

Move to the next level:

```text
level = 2
```



## Level 2

Queue:

```text
[7, 0]
```

Therefore:

```text
len_size = 2
```

Process:

```text
7
0
```

Calculate:

```text
level_sum = 7 + 0

level_sum = 7
```

Add their children:

```text
queue = [7, -8]
```

Compare:

```text
level_sum = 7

max_sum = 1
```

Since:

```text
7 > 1
```

update:

```text
max_sum = 7

answer = 2
```

Move to:

```text
level = 3
```



## Level 3

Queue:

```text
[7, -8]
```

Therefore:

```text
len_size = 2
```

Process:

```text
7
-8
```

Calculate:

```text
level_sum = 7 + (-8)

level_sum = -1
```

Compare:

```text
-1 > 7
```

False.

So:

```text
max_sum = 7

answer = 2
```

No more nodes remain.

The loop ends.

Return:

```text
2
```



# Dry Run

| Level | Nodes | Level Sum | Max Sum | Answer |
|------:|-------|----------:|--------:|-------:|
| 1 | `1` | `1` | `1` | `1` |
| 2 | `7, 0` | `7` | `7` | `2` |
| 3 | `7, -8` | `-1` | `7` | `2` |

Final answer:

```text
2
```



# Why Do We Use `>` Instead of `>=`?

The problem asks for the **smallest level** when multiple levels have the same maximum sum.

Suppose:

```text
Level 1 sum = 5

Level 2 sum = 5
```

We should return:

```text
1
```

Because level 1 is smaller.

Our code uses:

```python
if level_sum > max_sum:
```

not:

```python
if level_sum >= max_sum:
```

Therefore, when the sum is equal, we do **not** update the answer.

The earlier level remains the answer.



# Why Does `level_size` Prevent Mixing Levels?

Suppose:

```text
        1
       / \
      2   3
     / \
    4   5
```

Initially:

```text
queue = [1]
```

We save:

```python
level_size = len(queue)
```

So:

```text
level_size = 1
```

We process only node `1`.

While processing it, we add:

```text
2
3
```

Now:

```text
queue = [2,3]
```

But we do **not** process them in the same loop because the loop was limited to:

```text
1 node
```

They are processed in the next level.

This is what allows BFS to calculate the sum separately for each level.



# Complexity

```text
Time : O(n)
```

Every node is processed once.

```text
Space : O(n)
```

The queue can contain up to `O(n)` nodes in the worst case.



# Common Mistakes

### ❌ Processing Until the Queue Becomes Empty

Wrong:

```python
while queue:
    curr_node = queue.pop(0)
```

This processes the entire tree but does not tell us where one level ends and another begins.

We need:

```python
level_size = len(queue)
```

and then process exactly that many nodes.



### ❌ Updating on Equal Sums

Wrong:

```python
if level_sum >= max_sum:
```

This can return a later level when the sums are equal.

Correct:

```python
if level_sum > max_sum:
```

This keeps the smallest level.



### ❌ Forgetting to Add Children

After processing a node, its children must be added:

```python
if curr_node.left is not None:
    queue.append(curr_node.left)

if curr_node.right is not None:
    queue.append(curr_node.right)
```

Otherwise, the traversal stops after the first level.



### ❌ Resetting `max_sum` Every Level

Wrong:

```python
max_sum = level_sum
```

This would only keep the current level's sum.

Instead, update it only when:

```python
level_sum > max_sum
```



### ❌ Confusing `level` With `level_size`

They have different purposes:

```text
level

→ Which level are we currently processing?

level_size

→ How many nodes belong to this level?
```



# Similar Problems

- Binary Tree Level Order Traversal
- Binary Tree Right Side View
- Average of Levels in Binary Tree
- Minimum Depth of Binary Tree
- Maximum Depth of Binary Tree



# Interview Takeaway

## Recognition

```text
Binary Tree

BFS

Level Order Traversal

Queue

Process One Level at a Time
```

## Core Trick

```text
Put Root in Queue

↓

Get Current Level Size

↓

Process Exactly That Many Nodes

↓

Calculate Level Sum

↓

Add Children to Queue

↓

Compare With Maximum Sum

↓

Move to Next Level

↓

Return Level With Maximum Sum
```
