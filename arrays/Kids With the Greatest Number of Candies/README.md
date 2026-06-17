# Kids With the Greatest Number of Candies (LeetCode 1431)

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,

and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 

they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

**Example 1:**

Input: candies = [2,3,5,1,3], extraCandies = 3

Output: [true,true,true,false,true] 

Explanation: If you give all extraCandies to:

- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
 
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
 
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
 
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
 
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

  
**Example 2:**

Input: candies = [4,2,1,1,2], extraCandies = 1

Output: [true,false,false,false,false] 

Explanation: There is only 1 extra candy.

Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.


**Example 3:**

Input: candies = [12,1,12], extraCandies = 10

Output: [true,false,true]
 

**Constraints:**

n == candies.length

2 <= n <= 100

1 <= candies[i] <= 100

1 <= extraCandies <= 50



## Pattern

**Array Traversal + Simulation**




## Recognition

Use this pattern when the question contains:

* Compare every element with a maximum value
* Check if condition holds for each element
* Return a boolean array
* Simulate an operation on every element



## Key Observation

Every kid receives **all** the extra candies individually.

Instead of comparing every kid with every other kid:

1. Find the maximum candies any kid currently has.
2. For each kid, check:

```text
candies[i] + extraCandies >= maximumCandies
```

If true → `True`

Else → `False`



## Intuition

Current candies:

```text
[2,3,5,1,3]

Maximum = 5
Extra = 3
```

Check every kid:

```text
2 + 3 = 5  ✅

3 + 3 = 6  ✅

5 + 3 = 8  ✅

1 + 3 = 4  ❌

3 + 3 = 6  ✅
```

Answer:

```text
[True, True, True, False, True]
```



## Algorithm

1. Find the maximum value in the array.
2. Create an empty result array.
3. Traverse the array.
4. If `candies[i] + extraCandies >= maximum`, append `True`.
5. Otherwise append `False`.
6. Return the result.



## Code

```python
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        maximum = max(candies)

        result = []

        for candy in candies:

            if candy + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)

        return result
```



## Walkthrough

### Example 1

```text
candies = [2,3,5,1,3]
extraCandies = 3

maximum = 5
```

Iteration:

```text
Kid 1

2 + 3 = 5

5 >= 5

append True

----------------

Kid 2

3 + 3 = 6

6 >= 5

append True

----------------

Kid 3

5 + 3 = 8

8 >= 5

append True

----------------

Kid 4

1 + 3 = 4

4 < 5

append False

----------------

Kid 5

3 + 3 = 6

6 >= 5

append True
```

Result

```text
[True, True, True, False, True]
```



## Dry Run

| Kid | Candies | After Extra | Greatest? | Result |
| --- | ------- | ----------- | --------- | ------ |
| 1   | 2       | 5           | Yes       | True   |
| 2   | 3       | 6           | Yes       | True   |
| 3   | 5       | 8           | Yes       | True   |
| 4   | 1       | 4           | No        | False  |
| 5   | 3       | 6           | Yes       | True   |



## Edge Cases

```text
candies = [4,2,1,1,2]

extraCandies = 1

maximum = 4

Result

[True, False, False, False, False]
```



```text
candies = [12,1,12]

extraCandies = 10

maximum = 12

Result

[True, False, True]
```



## Complexity

```text
Time  : O(n)

Space : O(n)
```

where

```text
n = number of kids
```



## Template

```python
maximum = max(array)

result = []

for value in array:

    if value + extraValue >= maximum:
        result.append(True)
    else:
        result.append(False)

return result
```



## Common Mistakes

❌ Comparing every kid with every other kid (`O(n²)`).

❌ Updating the maximum after giving extra candies.

❌ Using `>` instead of `>=`.

Multiple kids can have the greatest number of candies.



## Similar Problems

* Find Pivot Index
* Running Sum of 1D Array
* Richest Customer Wealth
* Find the Highest Altitude
* Maximum Number of Balloons



## Interview Takeaway

### Recognition

```text
maximum element
compare every element
boolean result
simulation
```

### Core Trick

```text
Find the maximum once.

For every element:

current + extra >= maximum

↓

True

Else

↓

False
```
