
# Leaf-Similar Trees (LeetCode 872)

You are given the roots of two binary trees.

A **leaf node** is a node that has:

```text
No left child

AND

No right child
```

The **leaf value sequence** of a binary tree is the values of all its leaf nodes, from **left to right**.

Two binary trees are **leaf-similar** if their leaf value sequences are exactly the same.

Return:

```text
True
```

if the two trees are leaf-similar.

Otherwise return:

```text
False
```

For example:

```text
        3
       / \
      5   1
     / \ / \
    6  2 9  8
```

The leaf nodes from left to right are:

```text
6, 2, 9, 8
```

Therefore the leaf value sequence is:

```text
[6,2,9,8]
```


## Example 1

```text
Input:

root1 = [3,5,1,6,2,9,8,null,null,7,4]

root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

Output:

True
```

Explanation

The leaf value sequence of `root1` is:

```text
[6,7,4,9,8]
```

The leaf value sequence of `root2` is:

```text
[6,7,4,9,8]
```

Both sequences are the same.

Therefore:

```text
True
```



## Example 2

```text
Input:

root1 = [1,2,3]

root2 = [1,3,2]

Output:

False
```

Explanation

The leaf sequence of `root1` is:

```text
[2,3]
```

The leaf sequence of `root2` is:

```text
[3,2]
```

The order is different.

Therefore:

```text
False
```



## Constraints

```text
1 <= Number of Nodes <= 200

0 <= Node.val <= 200
```



# Pattern

```text
Binary Tree

DFS

Recursion

Leaf Traversal

Array Comparison
```



# Recognition

Use this pattern when the problem involves:

- Finding all leaf nodes
- Traversing a binary tree from left to right
- Preserving traversal order
- Comparing values from two trees
- Collecting values during DFS



# Brute Force

## Intuition

Traverse both trees separately.

Store the values of their leaf nodes in two arrays.

Then compare the two arrays.

For example:

```text
Tree 1

6 → 7 → 4 → 9 → 8
```

and

```text
Tree 2

6 → 7 → 4 → 9 → 8
```

Both arrays are equal, so the trees are leaf-similar.



## Algorithm

1. Create an empty list for the first tree.
2. Create an empty list for the second tree.
3. Traverse the first tree using DFS.
4. Whenever a leaf node is found, append its value to the first list.
5. Traverse the second tree using DFS.
6. Whenever a leaf node is found, append its value to the second list.
7. Compare the two lists.
8. Return the result.



# Optimal Approach (DFS + Leaf Value Lists)

## Key Observation

We only care about **leaf nodes**.

A node is a leaf when:

```python
current_node.left is None
```

and

```python
current_node.right is None
```

So during DFS, whenever we find:

```text
No left child

AND

No right child
```

we add its value to the result list.



# Why Do We Traverse Left Before Right?

The problem requires the leaf values in **left-to-right order**.

Therefore, for every node:

```text
Visit Left Subtree

↓

Visit Right Subtree
```

For example:

```text
        1
       / \
      2   3
     / \   \
    4   5   6
```

The leaf sequence must be:

```text
[4,5,6]
```

So we must traverse:

```text
Left → Right
```



# How Do We Identify a Leaf?

A leaf has no children.

Therefore:

```python
if current_node.left is None and current_node.right is None:
```

means:

```text
Current node is a leaf.
```

Then we add:

```python
results.append(current_node.val)
```



# Intuition

For each tree:

```text
Start at root

↓

Check if current node is a leaf

↓

If yes, add its value

↓

Otherwise explore left subtree

↓

Then explore right subtree

↓

Continue until the entire tree is traversed
```

After doing this for both trees:

```text
Leaf sequence 1

vs

Leaf sequence 2
```

If they are equal:

```text
True
```

Otherwise:

```text
False
```



# Algorithm

1. Create two empty lists:

```python
r1 = []
r2 = []
```

2. Define a recursive function:

```python
traverse(current_node, results)
```

3. If the current node is a leaf:

```python
if current_node.left is None and current_node.right is None:
    results.append(current_node.val)
```

4. If the left child exists, recursively traverse it:

```python
if current_node.left is not None:
    traverse(current_node.left, results)
```

5. If the right child exists, recursively traverse it:

```python
if current_node.right is not None:
    traverse(current_node.right, results)
```

6. Return the result list.

7. Generate both leaf sequences:

```python
traverse(root1, r1)

traverse(root2, r2)
```

8. Compare the two lists:

```python
return r1 == r2
```



# Code

```python
class Solution(object):

    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        r1 = []
        r2 = []

        def traverse(current_node, results):

            if current_node.left is None and current_node.right is None:
                results.append(current_node.val)

            if current_node.left is not None:
                traverse(current_node.left, results)

            if current_node.right is not None:
                traverse(current_node.right, results)

            return results

        return traverse(root1, r1) == traverse(root2, r2)
```



# Walkthrough

## Example

```text
root1 = [3,5,1,6,2,9,8,null,null,7,4]
```

Tree:

```text
          3
        /   \
       5     1
      / \   / \
     6   2 9   8
        / \
       7   4
```



## Start Traversal

Start at:

```text
3
```

Node `3` is not a leaf.

So traverse the left subtree first.

```text
3
↓
5
```



## Node 5

Node `5` is not a leaf.

Traverse left:

```text
6
```

Node `6` has no children.

Therefore:

```text
6 is a leaf
```

Add:

```text
[6]
```



## Continue Right

Back at node `5`, traverse right:

```text
2
```

Node `2` has children:

```text
7
4
```

Traverse left:

```text
7
```

`7` is a leaf.

Add:

```text
[6,7]
```

Then traverse right:

```text
4
```

`4` is a leaf.

Add:

```text
[6,7,4]
```



## Continue to Node 1

After finishing the left subtree of `3`, traverse right:

```text
1
```

Its left child is:

```text
9
```

`9` is a leaf.

Add:

```text
[6,7,4,9]
```

Then visit:

```text
8
```

`8` is a leaf.

Final leaf sequence:

```text
[6,7,4,9,8]
```

The same process is performed for `root2`.

If the second sequence is also:

```text
[6,7,4,9,8]
```

then:

```text
[6,7,4,9,8] == [6,7,4,9,8]
```

Therefore:

```text
True
```



# Dry Run

For:

```text
root1
```

the traversal produces:

| Node Visited | Leaf? | Result |
|--------------|--------|--------|
| 3 | No | [] |
| 5 | No | [] |
| 6 | Yes | [6] |
| 2 | No | [6] |
| 7 | Yes | [6,7] |
| 4 | Yes | [6,7,4] |
| 1 | No | [6,7,4] |
| 9 | Yes | [6,7,4,9] |
| 8 | Yes | [6,7,4,9,8] |

Final sequence:

```text
[6,7,4,9,8]
```



# Understanding the Recursion

The traversal follows:

```text
Root

↓

Left Subtree

↓

Right Subtree
```

For the example:

```text
        3
       / \
      5   1
     / \ / \
    6  2 9  8
      / \
     7   4
```

The DFS order visits:

```text
3
↓
5
↓
6
↓
2
↓
7
↓
4
↓
1
↓
9
↓
8
```

But we only store leaf nodes:

```text
6
7
4
9
8
```

Therefore:

```text
[6,7,4,9,8]
```



# Why Do We Need Two Lists?

We need to compare the leaf sequences of two different trees.

So we create:

```python
r1 = []
r2 = []
```

The first traversal fills:

```text
r1
```

with the leaves of `root1`.

The second traversal fills:

```text
r2
```

with the leaves of `root2`.

Finally:

```python
traverse(root1, r1) == traverse(root2, r2)
```

checks whether the two sequences are exactly the same.



# Why Does List Comparison Work?

Python compares lists element by element.

For example:

```python
[6,7,4,9,8] == [6,7,4,9,8]
```

returns:

```text
True
```

But:

```python
[6,7,4,9,8] == [6,7,9,4,8]
```

returns:

```text
False
```

The order matters.

This matches the problem because the leaf values must appear in the same **left-to-right order**.



# Complexity

Let:

```text
n = number of nodes in root1

m = number of nodes in root2
```

Each tree is traversed once.

```text
Time : O(n + m)
```

The result lists store the leaf values.

```text
Space : O(n + m)
```

The recursion stack additionally uses:

```text
O(h1 + h2)
```

where `h1` and `h2` are the heights of the two trees.



# Common Mistakes

### ❌ Adding Every Node

Wrong:

```python
results.append(current_node.val)
```

for every node.

The problem only asks for **leaf nodes**.

Correct:

```python
if current_node.left is None and current_node.right is None:
    results.append(current_node.val)
```


### ❌ Checking Only One Child

Wrong:

```python
if current_node.left is None:
```

A node with no left child can still have a right child.

For example:

```text
1
 \
  2
```

Node `1` is not a leaf.

Correct:

```python
if current_node.left is None and current_node.right is None:
```



### ❌ Traversing Right Before Left

Wrong:

```python
traverse(current_node.right, results)

traverse(current_node.left, results)
```

This produces the leaf sequence in reverse order.

Correct:

```python
traverse(current_node.left, results)

traverse(current_node.right, results)
```



### ❌ Comparing the Trees Directly

The structure of the trees does not need to be the same.

For example:

```text
Tree 1

    1
   / \
  2   3
```

and:

```text
Tree 2

    1
   / \
  3   2
```

have different structures/order but their leaf sequences are:

```text
[2,3]
```

and:

```text
[3,2]
```

so they are not leaf-similar.

The problem is specifically about the **leaf value sequence**.



### ❌ Forgetting to Pass the Same Result List

The recursive calls must use:

```python
traverse(current_node.left, results)
```

and:

```python
traverse(current_node.right, results)
```

This allows all recursive calls to append into the same list.



# Similar Problems

- Binary Tree Preorder Traversal
- Binary Tree Inorder Traversal
- Binary Tree Postorder Traversal
- Maximum Depth of Binary Tree
- Same Tree
- Path Sum



# Interview Takeaway

## Recognition

```text
Binary Tree

DFS

Recursion

Leaf Nodes

Left-to-Right Traversal
```

## Core Trick

```text
Traverse Tree

↓

Check If Current Node Is a Leaf

↓

If Leaf, Add Its Value

↓

Traverse Left

↓

Traverse Right

↓

Build Leaf Sequence

↓

Compare Both Sequences
```

# One thing to remember from this problem

You don't need nonlocal here because lists are mutable.

This works:

```text
results.append(value)
```

because we're modifying the existing list.

Whereas with an integer:

```text
max_depth += 1
```

we're trying to reassign the variable, which is why nonlocal became relevant in our previous problem.
