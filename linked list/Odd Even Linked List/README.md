# Odd Even Linked List (LeetCode 328)

You are given the **head** of a singly linked list.

Rearrange the linked list so that:

- All nodes at **odd indices** come first.
- All nodes at **even indices** come after them.

The **relative order** of nodes within both groups must remain the same.

Return the reordered linked list.

> **Note**
>
> Odd and even refer to the **node positions (indices)**, **not the node values**.



## Example 1

```text
Input:

head = [1,2,3,4,5]

Output:

[1,3,5,2,4]
```

Explanation

```text
Odd positions:

1 → 3 → 5

Even positions:

2 → 4

Join them:

1 → 3 → 5 → 2 → 4
```



## Example 2

```text
Input:

head = [2,1,3,5,6,4,7]

Output:

[2,3,6,7,1,5,4]
```

Explanation

```text
Odd positions:

2 → 3 → 6 → 7

Even positions:

1 → 5 → 4

Attach the even list after the odd list.
```



## Constraints

```text
0 <= Number of Nodes <= 10^4

-10^6 <= Node.val <= 10^6
```



# Pattern

```text
Linked List

Pointer Manipulation

In-Place Rearrangement
```



# Recognition

Use this pattern when the problem involves:

- Rearranging a linked list
- Preserving relative order
- Splitting into two groups
- Connecting multiple linked lists
- Constant extra space



# Brute Force

## Intuition

Create two separate lists.

- One stores odd-position nodes.
- One stores even-position nodes.

Finally,

connect the odd list with the even list.



## Algorithm

1. Traverse the linked list.
2. Store odd nodes separately.
3. Store even nodes separately.
4. Connect the two lists.
5. Return the odd list.



## Why is it Slow?

Although traversal is linear,

creating extra storage violates the required

```text
O(1)
```

space complexity.



## Complexity

```text
Time : O(n)

Space : O(n)
```



# Optimal Approach (Two Pointers)

## Key Observation

The linked list is already ordered.

We only need to reconnect the pointers.

Maintain

- Odd list
- Even list

using two pointers.

Save the head of the even list because it must be attached at the end.



# Why Save the Even Head?

Suppose

```text
1 → 2 → 3 → 4 → 5
```

Initially

```text
Odd

↓

1

Even

↓

2
```

During rearrangement,

the even pointer keeps moving.

If we don't save

```text
2
```

we lose the starting node of the even list.



# Why Skip One Node?

Suppose

```text
1 → 2 → 3 → 4 → 5
```

Odd pointer

```text
1
```

should connect to

```text
3
```

So

```python
odd.next = even.next
```

Similarly,

even pointer

```text
2
```

should connect to

```text
4
```

using

```python
even.next = odd.next
```

Each pointer skips one node.



# Intuition

Keep three pointers.

```text
odd

even

evenHead
```

Move odd through all odd-position nodes.

Move even through all even-position nodes.

After reaching the end,

attach

```text
odd.next = evenHead
```



# Algorithm

1. If the list is empty,

```text
Return head
```

2. Initialize

```text
odd = head

even = head.next

evenHead = even
```

3. While even and even.next exist:

- Connect odd to the next odd node.
- Move odd.
- Connect even to the next even node.
- Move even.

4. Attach the even list after the odd list.

5. Return head.



# Code

```python
class Solution(object):

    def oddEvenList(self, head):

        if not head:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head
```


# Walkthrough

## Example

```text
head = [1,2,3,4,5]
```

Initial

```text
Odd

1

Even

2

Even Head

2
```

List

```text
1 → 2 → 3 → 4 → 5
```



## Iteration 1

Connect odd

```text
1 → 3
```

Move odd

```text
Odd = 3
```

Connect even

```text
2 → 4
```

Move even

```text
Even = 4
```

List becomes

```text
1 → 3 → 4 → 5

2 → 4 → 5
```



## Iteration 2

Connect odd

```text
3 → 5
```

Move odd

```text
Odd = 5
```

Connect even

```text
4 → None
```

Move even

```text
Even = None
```

Attach

```text
5 → 2
```

Final list

```text
1 → 3 → 5 → 2 → 4
```



# Dry Run

| Odd | Even | Action |
| ---- | ---- | ------ |
| 1 | 2 | Start |
| 3 | 4 | Connect odd and even |
| 5 | None | Attach even list |



# Complexity

```text
Time : O(n)
```

Each node is visited only once.

```text
Space : O(1)
```

Only three pointers are used.



# Common Mistakes

### ❌ Using node values instead of positions

Wrong

```text
Odd values first

Even values later
```

The problem asks for

```text
Odd indices

Even indices
```



### ❌ Forgetting to save the even head

Wrong

```python
even = head.next
```

Without

```python
evenHead = even
```

the start of the even list is lost.



### ❌ Forgetting the final connection

Wrong

```python
return head
```

without

```python
odd.next = evenHead
```

The even nodes become disconnected.



### ❌ Wrong loop condition

Wrong

```python
while even:
```

Eventually,

```python
even.next
```

may become

```text
None
```

causing an error.

Use

```python
while even and even.next:
```



### ❌ Creating new nodes

The problem only asks to

```text
Rearrange pointers.
```

Do **not** create another linked list.



# Similar Problems

- Partition List
- Reorder List
- Swap Nodes in Pairs
- Reverse Linked List II
- Rotate List



# Interview Takeaway

## Recognition

```text
Linked List

Pointer Manipulation

In-Place Rearrangement

Two Pointers
```

## Core Trick

```text
Separate Odd List

↓

Separate Even List

↓

Preserve Relative Order

↓

Attach Even List At End

↓

Return Head
```
