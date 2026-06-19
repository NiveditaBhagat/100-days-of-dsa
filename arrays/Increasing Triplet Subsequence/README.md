# Increasing Triplet Subsequence (LeetCode 334)

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].

If no such indices exists, return false.

 

**Example 1:**

Input: nums = [1,2,3,4,5]

Output: true

Explanation: Any triplet where i < j < k is valid.

**Example 2:**

Input: nums = [5,4,3,2,1]

Output: false

Explanation: No triplet exists.

**Example 3:**

Input: nums = [2,1,5,0,4,6]

Output: true

Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
 

**Constraints:**

1 <= nums.length <= 5 * 105

-231 <= nums[i] <= 231 - 1

## Pattern

**Greedy | Prefix Minimum Tracking**


## Problem

Given an integer array `nums`, return `true` if there exists an increasing triplet

```text
(i, j, k)

such that

i < j < k

and

nums[i] < nums[j] < nums[k]
```

Otherwise, return `false`.



# Intuition

We do **NOT** need to find the actual triplet.

We only need to know whether one exists.

So instead of checking every combination, we keep track of the **smallest** and **second smallest** numbers seen so far.

If we ever find a number greater than both,

```text
first < second < current
```

then an increasing triplet exists.



# Key Idea

Maintain two variables:

```python
first = infinity
second = infinity
```

where

```text
first  -> smallest number seen so far

second -> smallest possible second element of a triplet
```



# Approach

Traverse the array once.

### Case 1

If current number is smaller than `first`

```python
first = num
```

Update the smallest element.



### Case 2

Else if current number is smaller than or equal to `second`

```python
second = num
```

We found a better second element.



### Case 3

Else

```text
num > second > first
```

which means

```text
first < second < num
```

An increasing triplet exists.

Return `True`.



# Code

```python
class Solution(object):

    def increasingTriplet(self, nums):

        first = float('inf')
        second = float('inf')

        for num in nums:

            if num <= first:

                first = num

            elif num <= second:

                second = num

            else:

                return True

        return False
```



# Walkthrough

## Example 1

```text
nums = [2,1,5,0,4,6]
```

Initial

```text
first = ∞

second = ∞
```



### num = 2

```text
2 <= first

first = 2
```

```text
first = 2

second = ∞
```



### num = 1

```text
1 <= first

first = 1
```

```text
first = 1

second = ∞
```



### num = 5

```text
5 > first

5 <= second

second = 5
```

```text
first = 1

second = 5
```



### num = 0

```text
0 <= first

first = 0
```

```text
first = 0

second = 5
```

Notice that second is **not reset**.

We still keep a possible second value.



### num = 4

```text
4 > first

4 <= second

second = 4
```

```text
first = 0

second = 4
```

Even better second element found.



### num = 6

```text
6 > first

6 > second
```

Therefore,

```text
0 < 4 < 6
```

Return

```text
True
```



# Dry Run

| Current Number | First | Second | Action |
|---------------|---------|---------|---------------------------|
|2|2|∞|Update first|
|1|1|∞|Update first|
|5|1|5|Update second|
|0|0|5|Update first|
|4|0|4|Update second|
|6|0|4|Found triplet → True|



# Why Use `<=` Instead of `<`?

Suppose

```text
nums = [1,1,2,3]
```

Using

```python
if num < first
```

the second `1` would go into `second`.

Then

```text
first = 1

second = 1
```

which is invalid because

```text
1 < 1
```

is false.

Using

```python
if num <= first
```

updates `first` instead,

keeping the smallest possible values.



# Why `float('inf')`?

Initialize with

```python
first = float('inf')
second = float('inf')
```

because every real number is smaller than infinity.

This allows the first comparisons to work naturally without special cases.



# Complexity

```text
Time Complexity  : O(n)

Space Complexity : O(1)
```

Only one traversal and two variables.



# Common Mistakes

### ❌ Brute Force

```text
Try every triplet

O(n³)
```

Too slow.



### ❌ Nested Loops

```text
Find increasing pair

Then search again

O(n²)
```

Still exceeds limits.



### ❌ Resetting second when first changes

Example

```text
[2,1,5,0,4,6]
```

If you reset second,

you lose valuable information and may miss a valid triplet.



# Pattern Recognition

Questions that ask

```text
Increasing subsequence

Minimum tracking

Can a sequence exist?

Need only True/False

One pass solution
```

often use a **Greedy + Running Minimum** approach.



# Similar Problems

- Longest Increasing Subsequence
- Best Time to Buy and Sell Stock
- Maximum Difference Between Increasing Elements
- Product of Array Except Self
- Jump Game



# Interview Takeaway

```text
Track the smallest number

↓

Track the smallest possible second number

↓

If a number is bigger than both

↓

Increasing Triplet Exists

↓

Return True
```



# Memory Trick

```text
first

↓

second

↓

current

If

current > second

then

first < second < current

✓ Triplet Found
```
