# Product of Array Except Self (LeetCode 238)


Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

**Example 1:**

Input: nums = [1,2,3,4]

Output: [24,12,8,6]

**Example 2:**

Input: nums = [-1,1,0,-3,3]

Output: [0,0,9,0,0]
 

**Constraints:**

2 <= nums.length <= 105

-30 <= nums[i] <= 30

The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


## Pattern

**Prefix Product + Suffix Product**



# Problem

Given an integer array `nums`, return an array `answer` such that

```text
answer[i] = product of all elements except nums[i]
```

### Constraints

- Do **NOT** use division.
- Time Complexity must be **O(n)**.



# Intuition

For every index, we need:

```text
Product of Left Elements

×

Product of Right Elements
```

Instead of calculating them every time, we make:

- One left-to-right traversal (Prefix)
- One right-to-left traversal (Suffix)

The answer array itself stores the prefix product, so no extra prefix array is needed.



# Approach

## Step 1 : Prefix Traversal

Maintain a running prefix product.

```text
prefix = 1
```

For every index,

```python
res[i] *= prefix
prefix *= nums[i]
```

So `res[i]` stores the product of all elements before index `i`.



## Step 2 : Suffix Traversal

Maintain a running suffix product.

```text
suffix = 1
```

Traverse from right to left.

For every index,

```python
res[i] *= suffix
suffix *= nums[i]
```

Now,

```text
res[i]

=

Prefix Product

×

Suffix Product
```

which is exactly the required answer.



# Code

```python
class Solution(object):

    def productExceptSelf(self, nums):

        n = len(nums)

        res = [1] * n

        prefix = 1

        # Prefix Product
        for i in range(n):

            res[i] *= prefix

            prefix *= nums[i]

        suffix = 1

        # Suffix Product
        for i in range(n - 1, -1, -1):

            res[i] *= suffix

            suffix *= nums[i]

        return res
```



# Example

```text
nums = [1,2,3,4]
```



## Prefix Pass

Initial

```text
res = [1,1,1,1]

prefix = 1
```

### i = 0

```text
res[0] = 1 × 1 = 1

prefix = 1 × 1 = 1
```

```text
res

[1,1,1,1]
```



### i = 1

```text
res[1] = 1 × 1 = 1

prefix = 1 × 2 = 2
```

```text
res

[1,1,1,1]
```



### i = 2

```text
res[2] = 1 × 2 = 2

prefix = 2 × 3 = 6
```

```text
res

[1,1,2,1]
```



### i = 3

```text
res[3] = 1 × 6 = 6

prefix = 6 × 4 = 24
```

```text
res

[1,1,2,6]
```



Now every index stores the **left product**.

```text
Index 0 → 1

Index 1 → 1

Index 2 → 1×2 = 2

Index 3 → 1×2×3 = 6
```



# Suffix Pass

Initial

```text
suffix = 1
```



### i = 3

```text
res[3] = 6 × 1 = 6

suffix = 1 × 4 = 4
```

```text
res

[1,1,2,6]
```



### i = 2

```text
res[2] = 2 × 4 = 8

suffix = 4 × 3 = 12
```

```text
res

[1,1,8,6]
```



### i = 1

```text
res[1] = 1 × 12 = 12

suffix = 12 × 2 = 24
```

```text
res

[1,12,8,6]
```



### i = 0

```text
res[0] = 1 × 24 = 24

suffix = 24 × 1 = 24
```

Final Answer

```text
[24,12,8,6]
```



# Dry Run

| Index | Prefix | Result Array | Suffix |
|------------|------------|----------------|------------|
|Start|1|[1,1,1,1]|1|
|i=0|1|[1,1,1,1]|-|
|i=1|2|[1,1,1,1]|-|
|i=2|6|[1,1,2,1]|-|
|i=3|24|[1,1,2,6]|-|
|i=3|-|[1,1,2,6]|4|
|i=2|-|[1,1,8,6]|12|
|i=1|-|[1,12,8,6]|24|
|i=0|-|[24,12,8,6]|24|



# Complexity

```text
Time Complexity : O(n)

Space Complexity : O(1)
```

> The output array is not counted as extra space.



# Why Initialize `res` with 1?

```python
res = [1] * n
```

Because

```text
1 × x = x
```

If initialized with `0`

```text
0 × prefix = 0

0 × suffix = 0
```

and every answer would remain zero.



# Why Use `*=`

```python
res[i] *= prefix
```

stores the left product.

Later,

```python
res[i] *= suffix
```

multiplies it with the right product.

So,

```text
res[i]

=

Left Product

×

Right Product
```

without creating separate prefix and suffix arrays.



# Common Mistakes

❌ Using division

```python
total_product // nums[i]
```

(Not allowed)



❌ Creating separate prefix and suffix arrays

```text
prefix[]

suffix[]

answer[]
```

Uses unnecessary extra space.



❌ Initializing

```python
res = [0] * n
```

which makes every multiplication equal to zero.



# Pattern

```text
Prefix Product

↓

Store in Answer Array

↓

Suffix Product

↓

Multiply with Existing Prefix

↓

Final Answer
```



# Similar Problems

- Running Sum of 1D Array
- Maximum Product Subarray
- Trapping Rain Water
- Best Time to Buy and Sell Stock
- Prefix Sum



# Interview Takeaway

```text
Need product except self

↓

Need left product

+

Need right product

↓

First pass stores prefix

↓

Second pass multiplies suffix

↓

O(n) Time

O(1) Extra Space
```
