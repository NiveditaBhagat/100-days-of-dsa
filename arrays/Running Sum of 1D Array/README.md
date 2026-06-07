# Running Sum of 1d Array 


Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
 
**Example 1:**

Input: nums = [1,2,3,4]

Output: [1,3,6,10]

Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


**Example 2:**

Input: nums = [1,1,1,1,1]

Output: [1,2,3,4,5]

Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].


**Example 3:**

Input: nums = [3,1,2,10,1]

Output: [3,4,6,16,17]
 

**Constraints:**

1 <= nums.length <= 1000

-10^6 <= nums[i] <= 10^6



## ✅ Approach 1: Modify the Input Array (Most Efficient)

* Start from index 1

* Add previous value to current value

* Return the same array





## 🧪 Example Walkthrough

**Input:**

```python
nums = [1, 2, 3, 4]
```

| Iteration | Operation | Updated Array |
|-----------|-----------|---------------|
| Initial | — | `[1, 2, 3, 4]` |
| `i = 1` | `nums[1] = nums[1] + nums[0] = 2 + 1 = 3` | `[1, 3, 3, 4]` |
| `i = 2` | `nums[2] = nums[2] + nums[1] = 3 + 3 = 6` | `[1, 3, 6, 4]` |
| `i = 3` | `nums[3] = nums[3] + nums[2] = 4 + 6 = 10` | `[1, 3, 6, 10]` |

### ✅ Result

```python
[1, 3, 6, 10]
```



## ⏱ Complexity (Approach 1)

Time: O(n)

Space: O(1) 





## ⏱ Complexity (Approach 2)

Time: O(n)

Space: O(n)


## 🚨 Common Mistakes

❌ Recalculating sum for every index (O(n²))

❌ Using nested loops

❌ Forgetting to start from index 1 in in-place method


## 🧠 Pattern to Remember

🔑 Prefix Sum Pattern

**Used in:**

* Running Sum of 1D Array

* Range Sum Query

* Subarray Sum Equals K
  
* Maximum Subarray
  
* Product of Array Except Self
