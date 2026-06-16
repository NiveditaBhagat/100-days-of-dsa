# Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 

If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

**Example 1:**

Input: word1 = "abc", word2 = "pqr"

Output: "apbqcr"

Explanation: The merged string will be merged as so:

word1:  a   b   c

word2:    p   q   r

merged: a p b q c r


**Example 2:**

Input: word1 = "ab", word2 = "pqrs"

Output: "apbqrs"

Explanation: Notice that as word2 is longer, "rs" is appended to the end.

word1:  a   b 

word2:    p   q   r   s

merged: a p b q   r   s


**Example 3:**

Input: word1 = "abcd", word2 = "pq"

Output: "apbqcd"

Explanation: Notice that as word1 is longer, "cd" is appended to the end.

word1:  a   b   c   d

word2:    p   q 

merged: a p b q c   d
 

**Constraints:**

1 <= word1.length, word2.length <= 100

word1 and word2 consist of lowercase English letters.



# Merge Strings Alternately (LeetCode 1768)

## Pattern

**Two Pointers / Parallel Traversal**



## Recognition

Use this pattern when the question contains:

* Merge two strings/arrays
* Alternate elements
* Interleave characters
* Take one element from each structure



## Intuition

Traverse both strings simultaneously.

* Take one character from `word1`
* Take one character from `word2`
* If one string ends, append the remaining characters from the other string.



## Algorithm

1. Find the maximum length of both strings.
2. Loop from `0` to `max_length - 1`.
3. If the index exists in `word1`, append that character.
4. If the index exists in `word2`, append that character.
5. Return the merged string.


## Code

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):

        result = ""

        max_len = max(len(word1), len(word2))

        for i in range(max_len):

            if i < len(word1):
                result += word1[i]

            if i < len(word2):
                result += word2[i]

        return result
```



## Walkthrough

### Example

```
word1 = "ab"
word2 = "pqrs"

result = ""

i = 0
append a -> "a"
append p -> "ap"

i = 1
append b -> "apb"
append q -> "apbq"

i = 2
word1 finished
append r -> "apbqr"

i = 3
word1 finished
append s -> "apbqrs"

Output = "apbqrs"
```



## Dry Run

| i | Action     | Result |
| - | ---------- | ------ |
| 0 | append a,p | ap     |
| 1 | append b,q | apbq   |
| 2 | append r   | apbqr  |
| 3 | append s   | apbqrs |



## Edge Cases

```
word1 = "abc"
word2 = "pqr"

Output:
apbqcr
```

```
word1 = "ab"
word2 = "pqrs"

Output:
apbqrs
```

```
word1 = "abcd"
word2 = "pq"

Output:
apbqcd
```

```
word1 = "a"
word2 = "b"

Output:
ab
```



## Complexity

```
Time  : O(m + n)

Space : O(m + n)
```

where

m = length of word1

n = length of word2



## Template

```python
result = ""

for i in range(max(len(first), len(second))):

    if i < len(first):
        result += first[i]

    if i < len(second):
        result += second[i]

return result
```



## Common Mistakes

❌ Loop only until the smaller string length.

❌ Forget to append remaining characters.

❌ Access an index without checking bounds.



## Similar Problems

* Merge Sorted Array
* Is Subsequence
* Valid Palindrome
* Move Zeroes
* Two Sum II



## Interview Takeaway

**Recognition:**

```
alternate
merge
interleave
zip
combine
```

**Idea:**

```
Traverse both structures together.
Check bounds before accessing.
Append remaining elements automatically.
```
