# Reverse Words in a String (LeetCode 151)


Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

**Example 1:**


Input: s = "the sky is blue"

Output: "blue is sky the"


**Example 2:**

Input: s = "  hello world  "

Output: "world hello"

Explanation: Your reversed string should not contain leading or trailing spaces.


**Example 3:**

Input: s = "a good   example"

Output: "example good a"

Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

**Constraints:**

1 <= s.length <= 104

s contains English letters (upper-case and lower-case), digits, and spaces ' '.

There is at least one word in s.


## Pattern

**String Manipulation + Split & Join**



## Recognition

Use this pattern when the question contains:

- Reverse words
- Ignore extra spaces
- Rearrange words
- Return a formatted string

Keywords:

```text
Reverse Words

Split

Join

Trim Spaces
```



## Key Observation

Python's `split()` automatically:

- Removes leading spaces
- Removes trailing spaces
- Converts multiple spaces into a single separator

After splitting:

1. Reverse the list of words.
2. Join them with a single space.



## Intuition

Input

```text
"  hello   world  "
```

### Step 1 : split()

```text
["hello", "world"]
```

Notice all extra spaces are removed.

### Step 2 : reverse

```text
["world", "hello"]
```

### Step 3 : join()

```text
"world hello"
```



## Algorithm

1. Split the string into words.
2. Reverse the list.
3. Join the words using a single space.
4. Return the result.



## Code

```python
class Solution(object):
    def reverseWords(self, s):

        words = s.split()

        words.reverse()

        return " ".join(words)
```



## One-Line Solution

```python
class Solution(object):
    def reverseWords(self, s):

        return " ".join(s.split()[::-1])
```



## Walkthrough

### Example 1

```text
Input

"the sky is blue"
```

Split

```text
["the","sky","is","blue"]
```

Reverse

```text
["blue","is","sky","the"]
```

Join

```text
"blue is sky the"
```



### Example 2

```text
Input

"  hello world  "
```

Split

```text
["hello","world"]
```

Reverse

```text
["world","hello"]
```

Join

```text
"world hello"
```



### Example 3

```text
Input

"a good   example"
```

Split

```text
["a","good","example"]
```

Reverse

```text
["example","good","a"]
```

Join

```text
"example good a"
```



## Dry Run

| Step | Result |
|----------------|-----------------------------|
|Original String|"  hello   world  "|
|split()|["hello","world"]|
|reverse()|["world","hello"]|
|" ".join()|"world hello"|



## Why does split() work?

```python
s = "  hello   world  "

print(s.split())
```

Output

```text
['hello', 'world']
```

It automatically:

✅ Removes leading spaces

✅ Removes trailing spaces

✅ Removes multiple spaces



## Complexity

```text
Time  : O(n)

Space : O(n)
```

where

```text
n = length of string
```



## Common Mistakes

❌ Using

```python
s.split(" ")
```

instead of

```python
s.split()
```

Example

```python
s = "  hello   world  "

s.split(" ")
```

Output

```text
['', '', 'hello', '', '', 'world', '', '']
```

which keeps empty strings.



❌ Forgetting to join using a single space

```python
"".join(words)
```

Output

```text
worldhello
```

Correct

```python
" ".join(words)
```

Output

```text
world hello
```



## Pattern Template

```python
words = s.split()

words.reverse()

return " ".join(words)
```

or

```python
return " ".join(s.split()[::-1])
```



## Similar Problems

- Reverse String
- Reverse Vowels of a String
- Merge Strings Alternately
- Valid Palindrome
- Length of Last Word



## Interview Takeaway

### Recognition

```text
Reverse Words

↓

Split into Words

↓

Reverse List

↓

Join with Single Space
```

### Core Trick

```text
split()

↓

Automatically removes extra spaces

↓

Reverse

↓

join()

↓

Final Answer
```



## Python Tricks Used

### split()

```python
"  hello   world ".split()

↓

["hello", "world"]
```

### reverse()

```python
words.reverse()
```

Reverses the list in-place.

### join()

```python
" ".join(words)
```

Joins all words with exactly one space.



## Interview Follow-up

If the interviewer asks:

> "Can you solve it without using split()?"

Pattern changes to:

```text
Two Pointers + String Traversal + Manual Word Extraction
```

which is a common follow-up for medium-level interviews.
