# Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


**Example 1:**

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.


**Example 2:**

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.


**Example 3:**

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


 
**Constraints:**

1 <= nums.length <= 105

-109 <= nums[i] <= 109




## 🧠 Key Insight (Core Idea)


**~Duplicates mean:**

An element appears more than once


**~To detect this efficiently:**

* Use a set

* Sets store only unique elements

* If an element already exists in the set → duplicate found




## 🪜 Approach (Using Hash Set)


Create an empty set seen


**Traverse the array:**


If the element is already in seen → return True

Else, add it to seen

If traversal finishes → return False



## ✅ Why This Works


Set lookup is O(1)


The moment we see a repeated value, we stop


No need to compare every pair



## 🧪 Example Walkthrough

**Input:**

```python
nums = [1, 2, 3, 1]
```

| Step | Seen Set | Current Element | Duplicate? |
|------|----------|----------------|------------|
| 1 | `{}` | `1` | ❌ No |
| 2 | `{1}` | `2` | ❌ No |
| 3 | `{1, 2}` | `3` | ❌ No |
| 4 | `{1, 2, 3}` | `1` | ✅ Yes → Return `True` |

### 🔍 Explanation

- Add `1` to the set.
- Add `2` to the set.
- Add `3` to the set.
- `1` is already present in the set, so a duplicate exists.

**Output:**

```python
True
```




## ⏱ Time & Space Complexity

Time: O(n)

Space: O(n)




## 💡 Hint (For Recall)

“If set size is smaller than array size → duplicates exist.”

Alternate one-liner:

return len(nums) != len(set(nums))



## 🚫 Common Mistakes

❌ Nested loops → O(n²) (inefficient)

❌ Sorting just to check duplicates (extra cost)

❌ Forgetting set lookup is O(1)



## 🔑 Pattern Name (Important for Interviews)

Hashing

Set-based lookup

Duplicate detection


