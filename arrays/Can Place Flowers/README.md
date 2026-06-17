# Can Place Flowers (LeetCode 605)

You have a long flowerbed in which some of the plots are planted, and some are not. 

However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 

return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

**Example 1:**

Input: flowerbed = [1,0,0,0,1], n = 1

Output: true


**Example 2:**

Input: flowerbed = [1,0,0,0,1], n = 2

Output: false
 

**Constraints:**

1 <= flowerbed.length <= 2 * 104

flowerbed[i] is 0 or 1.

There are no two adjacent flowers in flowerbed.

0 <= n <= flowerbed.length



## Pattern

**Greedy + Array Traversal**



## Recognition

Use this pattern when the question contains:

* Place elements with restrictions
* No adjacent elements
* Maximum possible placement
* Simulation
* Greedy decision



## Key Observation

A flower can be planted only if:

```text
Current Plot == 0

AND

Left Plot == 0 (or doesn't exist)

AND

Right Plot == 0 (or doesn't exist)
```

If all conditions are satisfied:

```text
Plant flower

flowerbed[i] = 1

Decrease n
```

Greedily planting at the first available position always gives the maximum number of flowers.



## Intuition

Traverse the flowerbed from left to right.

For every empty plot:

1. Find its left neighbor.
2. Find its right neighbor.
3. If both are empty, plant a flower.
4. Update the flowerbed so future checks use the new state.



## Algorithm

1. Traverse the flowerbed.
2. Skip occupied plots (`1`).
3. For an empty plot (`0`):

   * If it is the first plot, assume left = `0`.
   * Otherwise left = previous plot.
   * If it is the last plot, assume right = `0`.
   * Otherwise right = next plot.
4. If left and right are both `0`:

   * Plant a flower.
   * Decrease `n`.
5. Return `n <= 0`.



## Code

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:

                if i == 0:
                    left = 0
                else:
                    left = flowerbed[i - 1]

                if i == len(flowerbed) - 1:
                    right = 0
                else:
                    right = flowerbed[i + 1]

                if left == 0 and right == 0:

                    flowerbed[i] = 1
                    n -= 1

        return n <= 0
```



## Walkthrough

### Example

```text
flowerbed = [1,0,0,0,1]

n = 1
```

### Iteration 1

```text
i = 0

flowerbed[i] = 1

Already occupied

Skip
```



### Iteration 2

```text
i = 1

Current = 0

Left = 1

Right = 0

Cannot plant
```



### Iteration 3

```text
i = 2

Current = 0

Left = 0

Right = 0

Plant flower

flowerbed

[1,0,1,0,1]

n = 0
```



### Iteration 4

```text
i = 3

Current = 0

Left = 1

Right = 1

Cannot plant
```



### Return

```text
n = 0

return True
```



## Dry Run

| Index | Left | Current | Right | Action       | Flowerbed |
| ----- | ---- | ------- | ----- | ------------ | --------- |
| 0     | -    | 1       | -     | Skip         | 1 0 0 0 1 |
| 1     | 1    | 0       | 0     | Cannot Plant | 1 0 0 0 1 |
| 2     | 0    | 0       | 0     | Plant        | 1 0 1 0 1 |
| 3     | 1    | 0       | 1     | Cannot Plant | 1 0 1 0 1 |
| 4     | -    | 1       | -     | Skip         | 1 0 1 0 1 |



## Edge Cases

```text
flowerbed = [0]

n = 1

Output = True
```



```text
flowerbed = [1]

n = 1

Output = False
```



```text
flowerbed = [0,0,0]

n = 2

Plant at index 0

Plant at index 2

Output = True
```



```text
flowerbed = [1,0,1]

n = 1

Output = False
```



## Complexity

```text
Time  : O(n)

Space : O(1)
```

where

```text
n = length of flowerbed
```



## Common Mistakes

❌ Forgetting the boundary conditions.

```python
if i == 0:
    left = 0

if i == len(flowerbed) - 1:
    right = 0
```



❌ Forgetting to update the flowerbed.

```python
flowerbed[i] = 1
```

Without updating, future decisions become incorrect.



❌ Only decreasing `n` without actually planting the flower.

---

## Similar Problems

* Jump Game
* Lemonade Change
* Gas Station
* Kids With the Greatest Number of Candies



## Interview Takeaway

### Recognition

```text
Greedy

Array Traversal

Simulation

Adjacent Constraint

Local Optimal Choice
```

### Core Trick

```text
If Current == 0

AND

Left == 0

AND

Right == 0

↓

Plant Flower

↓

Update flowerbed

↓

Decrease n

↓

Continue Traversal
```
