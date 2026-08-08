# Maximum Twin Sum of a Linked List (LeetCode 2130)

You are given the **head** of a singly linked list with an **even length**.

The `ith` node is the **twin** of the `(n - 1 - i)th` node.

For example, if:

```text
n = 4
```

then:

```text
Node 0 ↔ Node 3

Node 1 ↔ Node 2
```

The **twin sum** is the sum of a node and its twin.

Return the **maximum twin sum** of the linked list.



## Example 1

```text
Input:

head = [5,4,2,1]

Output:

6
```

Explanation

```text
5 ↔ 1

5 + 1 = 6


4 ↔ 2

4 + 2 = 6
```

All twin sums are:

```text
6, 6
```

Therefore, the maximum twin sum is:

```text
6
```



## Example 2

```text
Input:

head = [4,2,2,3]

Output:

7
```

Explanation

```text
4 ↔ 3

4 + 3 = 7


2 ↔ 2

2 + 2 = 4
```

Therefore, the maximum twin sum is:

```text
7
```



## Example 3

```text
Input:

head = [1,100]

Output:

101
```

Explanation

```text
1 ↔ 100

1 + 100 = 101
```

Therefore, the maximum twin sum is:

```text
101
```



## Constraints

```text
2 <= Number of Nodes <= 10^5

Number of Nodes is even.

1 <= Node.val <= 10^5
```



# Pattern

```text
Linked List

Fast & Slow Pointer

Reverse Linked List

Two Pointers
```



# Recognition

Use this pattern when the problem involves:

- Finding the middle of a linked list
- Comparing nodes from opposite ends
- Pairing the first half with the second half in reverse order
- Reversing part of a linked list
- O(1) extra space



# Brute Force

## Intuition

Store all node values in an array.

Then use two pointers:

```text
left
```

starts from the beginning.

```text
right
```

starts from the end.

Calculate the sum of both values.



## Algorithm

1. Traverse the linked list.
2. Store all node values in an array.
3. Set:

```python
left = 0
right = n - 1
```

4. Calculate:

```python
arr[left] + arr[right]
```

5. Keep track of the maximum sum.
6. Move both pointers toward the middle.
7. Return the maximum twin sum.



## Why is it Not Ideal?

The problem can be solved without storing the entire linked list in an array.

The array requires:

```text
O(n)
```

extra space.

We can instead reverse the second half of the linked list in-place.



## Complexity

```text
Time : O(n)

Space : O(n)
```



# Optimal Approach (Fast & Slow Pointer + Reverse Second Half)

## Key Observation

Twin nodes are located symmetrically from both ends.

For:

```text
5 → 4 → 2 → 1
```

the twin pairs are:

```text
5 ↔ 1

4 ↔ 2
```

If we find the middle and reverse the second half:

```text
Original:

5 → 4 | 2 → 1
```

becomes:

```text
First Half:

5 → 4


Reversed Second Half:

1 → 2
```

Now the twin nodes are aligned in the same direction.

```text
5 ↔ 1

4 ↔ 2
```

We can use two pointers to calculate the sums.



# Step 1: Find the Middle

Use the **slow and fast pointer** technique.

```text
slow → moves 1 step

fast → moves 2 steps
```

For:

```text
5 → 4 → 2 → 1
```

the pointers eventually reach:

```text
5 → 4 | 2 → 1
       ↑
      slow
```

`slow` points to the first node of the second half.



# Step 2: Reverse the Second Half

The second half is:

```text
2 → 1
```

Reverse it:

```text
1 → 2
```

Now the list is conceptually divided into:

```text
First Half:

5 → 4


Reversed Second Half:

1 → 2
```



# Step 3: Calculate Twin Sums

Set:

```python
left = head
right = prev
```

where `prev` is the head of the reversed second half.

Now calculate:

```python
left.val + right.val
```

For every pair.

Example:

```text
5 + 1 = 6

4 + 2 = 6
```

Keep track of the maximum.



# Why Do We Reverse the Second Half?

Without reversing:

```text
First Half:

5 → 4


Second Half:

2 → 1
```

The nodes do not line up with their twins.

The correct pairs are:

```text
5 ↔ 1

4 ↔ 2
```

After reversing:

```text
First Half:

5 → 4


Second Half:

1 → 2
```

Now we can compare corresponding nodes directly.



# Intuition

The complete process is:

```text
Find Middle

↓

Reverse Second Half

↓

Compare First Half
with
Reversed Second Half

↓

Calculate Twin Sums

↓

Keep Maximum
```

No array is required.

The existing linked list nodes are reused.



# Algorithm

1. Initialize:

```python
slow = head
fast = head
```

2. Find the middle:

```python
while fast and fast.next:

    slow = slow.next
    fast = fast.next.next
```

3. Reverse the second half starting from `slow`.

4. Initialize:

```python
left = head
right = prev
maximum = 0
```

5. While `right` exists:

   - Calculate the twin sum.

   ```python
   current_sum = left.val + right.val
   ```

   - Update the maximum.

   ```python
   maximum = max(maximum, current_sum)
   ```

   - Move both pointers forward.

6. Return `maximum`.



# Code

```python
class Solution(object):

    def pairSum(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:

            nxt = curr.next

            curr.next = prev

            prev = curr
            curr = nxt

        left = head
        right = prev

        maximum = 0

        while right:

            current_sum = left.val + right.val

            maximum = max(maximum, current_sum)

            left = left.next
            right = right.next

        return maximum
```



# Walkthrough

## Example

```text
head = [5,4,2,1]
```

Initial list:

```text
5 → 4 → 2 → 1
```



## Step 1: Find Middle

Initially:

```text
slow = 5

fast = 5
```

After the first iteration:

```text
slow = 4

fast = 2
```

After the second iteration:

```text
slow = 2

fast = None
```

So:

```text
5 → 4 | 2 → 1
       ↑
      slow
```

The second half starts at:

```text
2
```



## Step 2: Reverse Second Half

Original:

```text
2 → 1
```

After reversal:

```text
1 → 2
```

Now:

```text
First Half:

5 → 4


Reversed Second Half:

1 → 2
```



## Step 3: Calculate Twin Sums

First pair:

```text
5 + 1 = 6
```

Maximum:

```text
6
```

Second pair:

```text
4 + 2 = 6
```

Maximum remains:

```text
6
```

Return:

```text
6
```



# Dry Run

| `left` | `right` | Twin Sum | Maximum |
| ------ | ------- | -------- | ------- |
| 5      | 1       | 6        | 6       |
| 4      | 2       | 6        | 6       |



# Complexity

```text
Time : O(n)
```

The linked list is traversed a constant number of times.

```text
Space : O(1)
```

Only a few pointers are used.



# Common Mistakes

### ❌ Comparing the second half without reversing it

Wrong:

```text
5 ↔ 2

4 ↔ 1
```

The actual twin pairs are:

```text
5 ↔ 1

4 ↔ 2
```

The second half must be reversed first.



### ❌ Using node values to find the middle

The middle depends on the **position of the nodes**, not their values.

Use:

```python
slow
fast
```

to find the middle.



### ❌ Changing `curr.next` before saving it

Wrong:

```python
curr.next = prev
nxt = curr.next
```

After changing the pointer,

the original next node is lost.

Always do:

```python
nxt = curr.next
curr.next = prev
```



### ❌ Returning the last twin sum

Wrong:

```python
return current_sum
```

There can be multiple twin sums.

We need the **maximum**.

Use:

```python
maximum = max(maximum, current_sum)
```



### ❌ Using an array unnecessarily

An array works, but it requires:

```text
O(n)
```

extra space.

The optimal solution reverses the second half in-place and uses:

```text
O(1)
```

extra space.



# Similar Problems

- Middle of the Linked List
- Reverse Linked List
- Palindrome Linked List
- Reorder List
- Reverse Linked List II



# Interview Takeaway

## Recognition

```text
Linked List

Fast & Slow Pointer

Reverse Second Half

Two Pointers

In-Place Manipulation
```

## Core Trick

```text
Find Middle

↓

Reverse Second Half

↓

Pair First Half
with
Reversed Second Half

↓

Calculate Twin Sums

↓

Keep Maximum
```
