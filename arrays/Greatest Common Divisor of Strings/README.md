# Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

**Example 1:**

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"


**Example 2:**

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"


**Example 3:**

Input: str1 = "LEET", str2 = "CODE"

Output: ""


**Example 4:**

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""​​​​​​​

 

**Constraints:**

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.




## Pattern

**Math + String + GCD**



## Recognition

Use this pattern when the question contains:

* Largest common string
* Repeated pattern
* Divides string
* Repeating substring
* Common base string



## Key Observation

A common divisor string exists **only if**:

```text
str1 + str2 == str2 + str1
```

If both concatenations are different, return `""`.

Once verified, the answer length is:

```text
gcd(len(str1), len(str2))
```

Return the prefix of that length.



## Intuition

If

```text
str1 = ABCABC
str2 = ABC
```

Both are made by repeating `"ABC"`.

```
ABCABC
ABC
```

The largest repeating unit length is the **GCD of the lengths**.

```
len(str1) = 6
len(str2) = 3

gcd(6,3) = 3

answer = str1[:3] = "ABC"
```



## Algorithm

1. Check if `str1 + str2 == str2 + str1`.
2. If not equal, return `""`.
3. Find `gcd(len(str1), len(str2))`.
4. Return `str1[:gcd_length]`.



## Code

```python
from math import gcd

class Solution(object):
    def gcdOfStrings(self, str1, str2):

        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]
```



## Walkthrough

### Example 1

```text
str1 = ABCABC
str2 = ABC

str1 + str2

ABCABCABC

str2 + str1

ABCABCABC

Equal ✅
```

```
gcd(6,3) = 3

return str1[:3]

ABC
```



### Example 2

```text
str1 = ABABAB
str2 = ABAB

str1 + str2

ABABABABAB

str2 + str1

ABABABABAB

Equal ✅
```

```
gcd(6,4) = 2

return str1[:2]

AB
```



### Example 3

```text
str1 = LEET
str2 = CODE

str1 + str2

LEETCODE

str2 + str1

CODELEET

Not Equal ❌

return ""
```



## Dry Run

| str1   | str2 | Concatenation Equal? | gcd Length | Output |
| ------ | ---- | -------------------- | ---------- | ------ |
| ABCABC | ABC  | ✅                    | 3          | ABC    |
| ABABAB | ABAB | ✅                    | 2          | AB     |
| LEET   | CODE | ❌                    | -          | ""     |
| AAAAAB | AAA  | ❌                    | -          | ""     |



## Edge Cases

```text
str1 = A
str2 = A

Output = A
```

```text
str1 = ABCABC
str2 = ABC

Output = ABC
```

```text
str1 = LEET
str2 = CODE

Output = ""
```

```text
str1 = AAAAAB
str2 = AAA

Output = ""
```




## Complexity

```text
Time  : O(m + n)

Space : O(m + n)
```

where

```
m = len(str1)
n = len(str2)
```



## Template

```python
if first + second != second + first:
    return ""

length = gcd(len(first), len(second))

return first[:length]
```




## Common Mistakes

❌ Trying every possible substring.

❌ Forgetting to verify:

```python
str1 + str2 == str2 + str1
```

❌ Returning the GCD length without checking if both strings share the same repeating pattern.




## Similar Problems

* Repeated Substring Pattern
* Repeated String Match
* Longest Common Prefix
* Greatest Common Divisor (Math)
* Find the Index of the First Occurrence in a String




## Interview Takeaway

**Recognition Keywords**

```text
largest common string
repeated pattern
divides string
common base string
```

**Core Trick**

```text
1. Verify both strings come from the same repeating pattern.

2. Answer length = gcd(len(str1), len(str2)).

3. Return the prefix of that length.
```
