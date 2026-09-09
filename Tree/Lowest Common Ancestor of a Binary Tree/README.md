# Lowest Common Ancestor of a Binary Tree (LeetCode 236)

Given a binary tree, find the **lowest common ancestor (LCA)** of two given nodes `p` and `q`.

The lowest common ancestor is the lowest node in the tree that has both `p` and `q` as descendants.

A node can also be considered a descendant of itself.



## Example 1

```text
Input:

root = [3,5,1,6,2,0,8,null,null,7,4]

p = 5
q = 1

Output:

3
```

Explanation

```text
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

Node `3` is the lowest node that contains both `5` and `1` in its subtree.

Therefore:

```text
LCA = 3
```



## Example 2

```text
Input:

root = [3,5,1,6,2,0,8,null,null,7,4]

p = 5
q = 4

Output:

5
```

Explanation

```text
        3
       / \
      5   1
     / \
    6   2
       / \
      7   4
```

Node `4` is inside the subtree of node `5`.

Since a node can be a descendant of itself:

```text
LCA = 5
```



## Example 3

```text
Input:

root = [1,2]

p = 1
q = 2

Output:

1
```

Explanation

```text
    1
   /
  2
```

Node `1` is an ancestor of node `2`.

Therefore:

```text
LCA = 1
```



## Constraints

```text
2 <= Number of Nodes <= 10^5

-10^9 <= Node.val <= 10^9

All Node.val are unique

p != q

p and q will exist in the tree
```



# Pattern

```text
Binary Tree

Depth First Search

Recursion

Lowest Common Ancestor
```



# Recognition

Use this pattern when the problem asks:

- Find the common ancestor of two nodes
- Find the lowest/deepest common ancestor
- Determine whether two target nodes are in different subtrees
- Search for two nodes while returning information upward
- Find an ancestor relationship in a binary tree



# Brute Force

## Intuition

One approach is to find the path from the root to `p` and the path from the root to `q`.

Then compare both paths from the beginning.

The last common node is the LCA.

For example:

```text
Path to p:

3 → 5 → 2 → 4

Path to q:

3 → 5 → 2 → 7
```

The last common node is:

```text
2
```

Therefore:

```text
LCA = 2
```



## Complexity

```text
Time : O(n)

Space : O(n)
```

We need to store the paths.



# Optimal Approach (Recursive DFS)

## Key Observation

At every node, there are three important possibilities:

### Case 1: Current node is `p` or `q`

If:

```python
root == p or root == q
```

then return the current node.

This is important because one target node can itself be the LCA.



### Case 2: `p` and `q` are found in different subtrees

Suppose:

```text
        3
       / \
      5   1
```

If:

```text
p = 5
q = 1
```

then:

```text
left  → p found
right → q found
```

Therefore the current node:

```text
3
```

is the LCA.

So:

```python
if left is not None and right is not None:
    return root
```



### Case 3: Both nodes are found in the same subtree

If only the left subtree returns a node:

```python
if left is not None:
    return left
```

we return whatever the left subtree found.

Similarly, if only the right subtree returns a node:

```python
return right
```

The important idea is that the recursive call returns the LCA found below, if one exists.



# Intuition

For every node:

```text
Check if current node is p or q

↓

Search left subtree

↓

Search right subtree

↓

If both sides return a node

    ↓

Current node is LCA

↓

If only one side returns a node

    ↓

Return that node upward

↓

If neither side returns a node

    ↓

Return None
```



# Why Do We Return `root` When Both Sides Are Not None?

Suppose we have:

```text
        3
       / \
      5   1
```

and:

```text
p = 5
q = 1
```

When we are at node `3`:

```python
left = 5
right = 1
```

Both are not `None`.

That means:

```text
p exists somewhere in the left subtree

q exists somewhere in the right subtree
```

Therefore `3` is the first node where the two paths meet.

So:

```python
return root
```



# Why Do We Return `left` or `right`?

Suppose:

```text
        3
       /
      5
     / \
    6   2
```

and:

```text
p = 5
q = 4
```

Assume `4` is somewhere below `5`.

When recursion reaches `5`:

```python
root == p
```

so it immediately returns:

```text
5
```

That result travels back upward.

The parent nodes don't need to search further because the LCA has already been found.

This is why:

```python
if left is not None:
    return left

return right
```

works.



# Algorithm

1. If the current node is `None`, return:

```text
None
```

2. If the current node is `p` or `q`, return the current node.

3. Recursively search the left subtree:

```python
left = self.lowestCommonAncestor(root.left, p, q)
```

4. Recursively search the right subtree:

```python
right = self.lowestCommonAncestor(root.right, p, q)
```

5. If both `left` and `right` are not `None`, both nodes were found in different subtrees.

Return:

```python
root
```

6. If only `left` is not `None`, return:

```python
left
```

7. Otherwise return:

```python
right
```



# Code

```python
class Solution(object):

    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)

        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is not None:
            return left

        return right
```



# Walkthrough

## Example

```text
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

Let:

```text
p = 5

q = 1
```



## Start at Node 3

```text
root = 3
```

`3` is neither `p` nor `q`.

So search both subtrees:

```text
left  → subtree of 5

right → subtree of 1
```



## Search Left Subtree

At node:

```text
5
```

We have:

```text
root == p
```

Therefore:

```python
return 5
```

So:

```text
left = 5
```



## Search Right Subtree

At node:

```text
1
```

We have:

```text
root == q
```

Therefore:

```python
return 1
```

So:

```text
right = 1
```



## Back at Node 3

Now:

```text
left  = 5

right = 1
```

Both are not `None`.

Therefore:

```python
if left is not None and right is not None:
    return root
```

Since:

```text
root = 3
```

we return:

```text
3
```

Therefore:

```text
LCA = 3
```



# Another Walkthrough

## Example

```text
        3
       /
      5
     / \
    6   2
       / \
      7   4
```

Let:

```text
p = 5

q = 4
```



## At Node 3

Node `3` is neither `p` nor `q`.

Search both sides.

The left subtree returns:

```text
5
```

The right subtree returns:

```text
None
```

So:

```text
left = 5

right = None
```

Only the left side found something.

Therefore:

```python
return left
```

which returns:

```text
5
```

So:

```text
LCA = 5
```



# Recursion Flow

For:

```text
        3
       / \
      5   1
```

with:

```text
p = 5
q = 1
```

The recursion effectively does:

```text
             3
           /   \
          5     1
          ↑     ↑
          p     q
          ↓     ↓
        return return
          5     1
           \   /
            \ /
             3
             ↑
          both found
             ↓
          return 3
```

The key idea is that information travels **back upward** through the recursion.



# Dry Run

| Current Node | Left Result | Right Result | Returned |
|--------------|-------------|--------------|----------|
| 5 | - | - | 5 |
| 1 | - | - | 1 |
| 3 | 5 | 1 | 3 |

For:

```text
p = 5
q = 4
```

the important flow is:

| Current Node | Result |
|--------------|--------|
| 5 | 5 |
| 3 | 5 |

The result `5` propagates upward because only the left subtree contains the targets.



# Why This Works

The recursion gives each node information about what was found below it.

For every node:

```text
None

→ Neither p nor q found
```

or:

```text
p / q / LCA

→ Something important was found below
```

When both sides return something:

```text
left != None

right != None
```

we know that the two target nodes are separated across the current node.

Therefore:

```text
current node = LCA
```

If only one side returns something, the LCA is still somewhere in that returned result.



# Complexity

```text
Time : O(n)
```

In the worst case, every node is visited once.

```text
Space : O(h)
```

where `h` is the height of the tree because of the recursion stack.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```



# Common Mistakes

### ❌ Returning `None` when the current node is `p` or `q`

Wrong:

```python
if root == p or root == q:
    return None
```

If we find one of the target nodes, we need to tell the parent recursion that it was found.

Correct:

```python
if root == p or root == q:
    return root
```



### ❌ Only searching one subtree

Wrong:

```python
left = self.lowestCommonAncestor(root.left, p, q)

return left
```

The two nodes might be on different sides.

We need to search both:

```python
left = self.lowestCommonAncestor(root.left, p, q)

right = self.lowestCommonAncestor(root.right, p, q)
```



### ❌ Returning the current node whenever one target is found

The current node is only the LCA when:

```text
left != None

AND

right != None
```

If only one side returns something, we propagate that result upward.



### ❌ Forgetting That a Node Can Be Its Own Ancestor

For:

```text
p = 5
q = 4
```

where `4` is below `5`:

```text
5
 \
  4
```

the LCA is:

```text
5
```

Therefore:

```python
if root == p or root == q:
    return root
```

is essential.



### ❌ Confusing This With a BST

This is a **Binary Tree**, not a Binary Search Tree.

We cannot use:

```text
p < root
q > root
```

to decide which direction to search.

We may need to search both subtrees.



# Similar Problems

- Lowest Common Ancestor of a Binary Search Tree
- Lowest Common Ancestor of a Deepest Leaves
- Smallest Common Region
- Kth Ancestor of a Tree Node
- Step-By-Step Directions From a Binary Tree Node to Another



# Interview Takeaway

## Recognition

```text
Binary Tree

DFS

Recursion

Ancestor / Subtree Problem
```

## Core Trick

```text
If Node is None

↓

Return None

↓

If Node is p or q

↓

Return Node

↓

Search Left

↓

Search Right

↓

If Both Sides Return Something

↓

Current Node is LCA

↓

If Only Left Returns Something

↓

Return Left

↓

Otherwise

↓

Return Right
```
