# Reverse Linked List (LeetCode 206)

You are given the **head** of a singly linked list.

Reverse the linked list and return the new head.

For example:

```text
1 → 2 → 3 → 4 → 5
```

becomes

```text
5 → 4 → 3 → 2 → 1
```



## Example 1

```text
Input:

head = [1,2,3,4,5]

Output:

[5,4,3,2,1]
```

Explanation

```text
Original:

1 → 2 → 3 → 4 → 5

Reverse every link:

5 → 4 → 3 → 2 → 1
```



## Example 2

```text
Input:

head = [1,2]

Output:

[2,1]
```

Explanation

```text
1 → 2

↓

2 → 1
```



## Example 3

```text
Input:

head = []

Output:

[]
```

Explanation

```text
There are no nodes.

Return None.
```



## Constraints

```text
0 <= Number of Nodes <= 5000

-5000 <= Node.val <= 5000
```



# Pattern

```text
Linked List

Pointer Manipulation

In-Place Reversal
```



# Recognition

Use this pattern when the problem involves:

- Reversing a linked list
- Changing the direction of links
- In-place modification
- Constant extra space
- Traversing nodes while modifying pointers



# Brute Force

## Intuition

Store all node values in an array.

Reverse the array.

Then create a new linked list using the reversed values.



## Algorithm

1. Traverse the linked list.
2. Store every value in an array.
3. Reverse the array.
4. Create a new linked list.
5. Return the new head.



## Why is it Not Ideal?

The problem can be solved by changing the existing links directly.

Creating an array and a new linked list requires extra memory.



## Complexity

```text
Time : O(n)

Space : O(n)
```



# Optimal Approach (Three Pointers)

## Key Observation

To reverse a linked list,

we need to reverse the direction of every

```text
next
```

pointer.

Suppose

```text
1 → 2 → 3 → None
```

We want

```text
None ← 1 ← 2 ← 3
```

The problem is that once we change

```python
curr.next
```

we can lose the rest of the list.

So we need to save it first.



# Why Do We Need `nxt`?

Suppose

```text
1 → 2 → 3
↑
curr
```

If we directly do

```python
curr.next = prev
```

the link to `2` is lost.

Therefore,

first save

```python
nxt = curr.next
```

Now we can safely reverse the current link.



# The Three Pointers

We use:

```text
prev

curr

nxt
```

Initially

```text
prev = None

curr = head
```

Then inside the loop:

```python
nxt = curr.next
curr.next = prev
prev = curr
curr = nxt
```

Each pointer has a specific job.



## `prev`

Points to the already reversed portion.

```text
None ← 1 ← 2
          ↑
         prev
```



## `curr`

Points to the node currently being reversed.

```text
3 → 4 → 5
↑
curr
```


## `nxt`

Temporarily saves the remaining list.

```text
3 → 4 → 5
    ↑
   nxt
```



# Intuition

At every step:

```text
Save the next node

↓

Reverse the current link

↓

Move prev forward

↓

Move curr forward
```

Eventually,

```text
curr = None
```

and

```text
prev
```

points to the new head.



# Algorithm

1. Initialize

```python
prev = None
curr = head
```

2. While `curr` exists:

   - Save the next node.

   ```python
   nxt = curr.next
   ```

   - Reverse the current pointer.

   ```python
   curr.next = prev
   ```

   - Move `prev`.

   ```python
   prev = curr
   ```

   - Move `curr`.

   ```python
   curr = nxt
   ```

3. When `curr` becomes `None`,

```text
prev
```

is the new head.

4. Return `prev`.



# Code

```python
class Solution(object):

    def reverseList(self, head):

        prev = None
        curr = head

        while curr:

            nxt = curr.next

            curr.next = prev

            prev = curr

            curr = nxt

        return prev
```



# Walkthrough

## Example

```text
head = [1,2,3,4,5]
```

Initial state

```text
prev = None

curr = 1
```

List

```text
1 → 2 → 3 → 4 → 5
```



## Iteration 1

Save next:

```text
nxt = 2
```

Reverse:

```text
1 → None
```

Move pointers:

```text
prev = 1

curr = 2
```

Remaining list:

```text
2 → 3 → 4 → 5
```



## Iteration 2

Save:

```text
nxt = 3
```

Reverse:

```text
2 → 1 → None
```

Move:

```text
prev = 2

curr = 3
```



## Iteration 3

Save:

```text
nxt = 4
```

Reverse:

```text
3 → 2 → 1 → None
```

Move:

```text
prev = 3

curr = 4
```



## Iteration 4

Save:

```text
nxt = 5
```

Reverse:

```text
4 → 3 → 2 → 1 → None
```

Move:

```text
prev = 4

curr = 5
```



## Iteration 5

Save:

```text
nxt = None
```

Reverse:

```text
5 → 4 → 3 → 2 → 1 → None
```

Move:

```text
prev = 5

curr = None
```

Loop ends.

Return

```text
prev
```

Final list:

```text
5 → 4 → 3 → 2 → 1
```



# Dry Run

| `prev` | `curr` | `nxt` | Reversed Portion |
| ------- | ------- | ------ | ---------------- |
| None | 1 | 2 | 1 → None |
| 1 | 2 | 3 | 2 → 1 → None |
| 2 | 3 | 4 | 3 → 2 → 1 → None |
| 3 | 4 | 5 | 4 → 3 → 2 → 1 → None |
| 4 | 5 | None | 5 → 4 → 3 → 2 → 1 |



# Complexity

```text
Time : O(n)
```

Every node is visited exactly once.

```text
Space : O(1)
```

Only three pointers are used.



# Common Mistakes

### ❌ Changing `curr.next` before saving it

Wrong

```python
curr.next = prev
nxt = curr.next
```

After changing the pointer,

the original next node is already lost.

Always do:

```python
nxt = curr.next
curr.next = prev
```



### ❌ Forgetting to move `curr`

Wrong

```python
curr.next = prev
prev = curr
```

`curr` must move to the saved next node:

```python
curr = nxt
```

Otherwise the loop never progresses.



### ❌ Returning `head`

Wrong

```python
return head
```

The original head is now the **last node**.

After reversal,

the new head is

```python
prev
```

So return:

```python
return prev
```



### ❌ Forgetting `prev = curr`

After reversing

```text
curr.next = prev
```

the current node becomes part of the reversed list.

Therefore:

```python
prev = curr
```

is necessary.



### ❌ Thinking `nxt` is another node

`nxt` is only a pointer/reference.

We are not creating a new node.

```text
nxt = curr.next
```

simply saves where the remaining list begins.



# Similar Problems

- Reverse Linked List II
- Reverse Nodes in k-Group
- Reorder List
- Palindrome Linked List
- Swap Nodes in Pairs



# Interview Takeaway

## Recognition

```text
Linked List

Pointer Manipulation

In-Place Reversal

Three Pointers
```

## Core Trick

```text
Save Next

↓

Reverse Current Link

↓

Move Prev

↓

Move Curr

↓

Repeat Until Curr Is None

↓

Prev Becomes New Head
```
