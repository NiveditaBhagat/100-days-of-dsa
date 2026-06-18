# Reverse Vowels of a String (LeetCode 345)



Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

**Example 1:**

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


**Example 2:**

Input: s = "leetcode"

Output: "leotcede"

 

**Constraints:**

1 <= s.length <= 3 * 105

s consist of printable ASCII characters.

## Pattern

**Two Pointers + String Manipulation**


## Recognition

Use this pattern when the question contains:

- Reverse only specific elements
- Two ends of an array/string
- Swap elements
- Skip unwanted characters

Keywords:

```text
Reverse
Swap
Left & Right
Skip Characters
```



## Key Observation

We only need to reverse the vowels.

- Left pointer searches for the next vowel.
- Right pointer searches for the previous vowel.
- When both point to vowels, swap them.
- Continue until the pointers meet.



## Intuition

Example:

```text
s = "IceCreAm"

           L           R
           I c e C r e A m
```

Vowels:

```text
[I, e, e, A]
```

Reverse vowels:

```text
[A, e, e, I]
```

Final string:

```text
AceCreIm
```




## Algorithm

1. Convert the string into a list.
2. Store all vowels in a set.
3. Initialize two pointers:
   - left = 0
   - right = len(s) - 1
4. Move left until it points to a vowel.
5. Move right until it points to a vowel.
6. Swap both vowels.
7. Move both pointers inward.
8. Convert the list back into a string.




## Code

```python
class Solution(object):
    def reverseVowels(self, s):

        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)
```



## Walkthrough

### Example 1

```text
s = "IceCreAm"
```

Initial

```text
I c e C r e A m
L             R
```

Right moves left

```text
I c e C r e A m
L           R
```

Swap

```text
A c e C r e I m
```

Move pointers

```text
A c e C r e I m
    L     R
```

Both already vowels

Swap

```text
A c e C r e I m
```

Pointers cross.

Return

```text
AceCreIm
```



### Example 2

```text
leetcode

Vowels

[e,e,o,e]

Reverse

[e,o,e,e]

Result

leotcede
```



## Dry Run

| Left | Right | Characters | Action |
|----------|-----------|----------------|----------------|
|0|6|I , A|Swap|
|1|5|c , e|Move Left|
|2|5|e , e|Swap|
|3|4|C , r|Move Both|
|End|-|Pointers Cross|Return|



## Edge Cases

```text
Input

"a"

Output

"a"
```



```text
Input

"bcdf"

Output

"bcdf"

(No vowels)
```



```text
Input

"aeiou"

Output

"uoiea"
```



```text
Input

"Aa"

Output

"aA"
```



## Complexity

```text
Time  : O(n)

Space : O(n)
```

- O(n) for converting the string into a list.
- Each pointer visits every character at most once.



## Common Mistakes

❌ Trying to modify a string directly.

```python
s[0] = 'a'
```

Strings are immutable in Python.

Always convert to a list first.



❌ Forgetting uppercase vowels.

```python
{'a','e','i','o','u'}
```

This will fail for:

```text
"IceCreAm"
```

Include both lowercase and uppercase vowels.



❌ Using a list instead of a set for vowel lookup.

```python
vowels = ['a','e','i','o','u']
```

Membership becomes O(5).

Use

```python
vowels = {'a','e','i','o','u'}
```

for O(1) lookup.



## Pattern Template

```python
left = 0
right = len(array) - 1

while left < right:

    while left < right and not valid_left:
        left += 1

    while left < right and not valid_right:
        right -= 1

    swap(left, right)

    left += 1
    right -= 1
```



## Similar Problems

- Valid Palindrome
- Two Sum II
- Move Zeroes
- Merge Strings Alternately
- Squares of a Sorted Array



## Interview Takeaway

### Recognition

```text
Reverse only selected characters

↓

Use Two Pointers

↓

Skip unwanted elements

↓

Swap valid elements
```

### Core Trick

```text
Left → Find Next Vowel

Right → Find Previous Vowel

↓

Swap

↓

Move Inward

↓

Repeat Until Left >= Right
```
