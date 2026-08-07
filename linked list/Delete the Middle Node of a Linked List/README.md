

# Delete the Middle Node of a Linked List (LeetCode 2095)

You are given the **head** of a singly linked list.

Delete the **middle node**, and return the head of the modified linked list.

The middle node is determined as:

```text
⌊ n / 2 ⌋
```

using **0-based indexing**.

If the list contains only **one node**, return

```text
None
```



## Example 1

```text
Input:

head = [1,3,4,7,1,2,6]

Output:

[1,3,4,1,2,6]
```

Explanation

```text
Length = 7

Middle index = 7 // 2 = 3

Node with value 7 is deleted.
```



## Example 2

```text
Input:

head = [1,2,3,4]

Output:

[1,2,4]
```

Explanation

```text
Length = 4

Middle index = 4 // 2 = 2

Node with value 3 is deleted.
```



## Example 3

```text
Input:

head = [2]

Output:

[]
```

Explanation

```text
The only node is also the middle node.

Return None.
```



## Constraints

```text
1 <= Number of Nodes <= 10^5

1 <= Node.val <= 10^5
```



# Pattern

```text
Linked List

Fast & Slow Pointer

Two Pointers
```



# Recognition

Use this pattern when the problem involves:

- Finding the middle of a linked list
- Single traversal
- Two pointers moving at different speeds
- Modifying links without extra space



# Brute Force

## Intuition

Traverse the linked list once to count the number of nodes.

Compute the middle index.

Traverse again until reaching the node just before the middle.

Skip the middle node.



## Algorithm

1. Count the total number of nodes.
2. Compute the middle index.
3. Traverse to the previous node.
4. Update its next pointer.
5. Return the head.



## Why is it Slow?

The linked list is traversed twice.

Although still linear, we can find the middle in a single traversal.



## Complexity

```text
Time : O(n)

Space : O(1)
```



# Optimal Approach (Fast & Slow Pointer)

## Key Observation

Move two pointers together.

- Slow moves one step.
- Fast moves two steps.

When the fast pointer reaches the end,

the slow pointer reaches the middle.

To delete the middle,

keep another pointer pointing to the node before slow.



# Why Does This Work?

Suppose

```text
1 → 3 → 4 → 7 → 1 → 2 → 6
```

Initially

```text
Slow

↓

1 → 3 → 4 → 7 → 1 → 2 → 6
↑
Fast
```

Every iteration

```text
Slow += 1 node

Fast += 2 nodes
```

When Fast reaches the end,

Slow is exactly at the middle.



# Why Keep a Previous Pointer?

Suppose

```text
Previous

↓

4 → 7 → 1
     ↑
   Slow
```

To delete 7,

we cannot move backward in a singly linked list.

Instead,

connect

```text
Previous.next

↓

1
```

using

```python
prev.next = slow.next
```



# Intuition

If the list has only one node,

return

```text
None
```

Otherwise,

use three pointers.

- prev
- slow
- fast

Move fast twice as quickly as slow.

Keep updating prev before moving slow.

When fast reaches the end,

slow points to the middle node.

Skip it.



# Algorithm

1. If the list has only one node,

```text
Return None
```

2. Initialize

```text
prev = None

slow = head

fast = head
```

3. While fast and fast.next exist:

- Move prev to slow.
- Move slow one step.
- Move fast two steps.

4. Delete the middle node using

```python
prev.next = slow.next
```

5. Return the head.



# Code

```python
class Solution(object):

    def deleteMiddle(self, head):

        if head.next is None:
            return None

        prev = None
        slow = head
        fast = head

        while fast and fast.next:

            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
```



# Walkthrough

## Example

```text
head = [1,3,4,7,1,2,6]
```

Initial pointers

```text
prev = None

slow = 1

fast = 1
```



## Iteration 1

Move

```text
prev = 1

slow = 3

fast = 4
```



## Iteration 2

Move

```text
prev = 3

slow = 4

fast = 1
```



## Iteration 3

Move

```text
prev = 4

slow = 7

fast = 6
```

Fast cannot move further.

Middle node

```text
7
```

Delete

```python
prev.next = slow.next
```

Result

```text
1 → 3 → 4 → 1 → 2 → 6
```



# Dry Run

| Prev | Slow | Fast | Action |
| ---- | ---- | ---- | ------ |
| None | 1 | 1 | Start |
| 1 | 3 | 4 | Move pointers |
| 3 | 4 | 1 | Move pointers |
| 4 | 7 | 6 | Delete middle |



# Complexity

```text
Time : O(n)
```

The linked list is traversed only once.

```text
Space : O(1)
```

Only a few pointers are used.



# Common Mistakes

### ❌ Forgetting the single-node case

Wrong

```python
prev.next = slow.next
```

If only one node exists,

```text
prev

↓

None
```

which causes an error.

Always handle

```python
if head.next is None:
    return None
```



### ❌ Moving slow before saving prev

Wrong

```python
slow = slow.next
prev = slow
```

Now prev points to the middle instead of the previous node.

Delete becomes impossible.



### ❌ Moving fast only one step

Wrong

```python
fast = fast.next
```

Then slow no longer reaches the middle correctly.



### ❌ Using

```python
slow = slow.next
```

to delete the node

This only moves the pointer.

It does **not** remove the node from the linked list.

You must change the link.

```python
prev.next = slow.next
```



### ❌ Forgetting to return head

After deletion,

the modified list still starts from

```text
head
```

Return

```python
head
```



# Similar Problems

- Middle of the Linked List
- Remove Nth Node From End of List
- Linked List Cycle
- Palindrome Linked List
- Reorder List



# Interview Takeaway

## Recognition

```text
Linked List

Fast & Slow Pointer

Two Pointers

Single Traversal
```

## Core Trick

```text
Fast Moves Two Steps

↓

Slow Moves One Step

↓

Slow Reaches Middle

↓

Keep Previous Pointer

↓

Skip Middle Node

↓

Return Head
```

