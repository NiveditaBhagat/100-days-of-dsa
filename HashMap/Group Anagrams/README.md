# Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

**Example 1:**

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".

The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.

The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

**Example 2:**

Input: strs = [""]

Output: [[""]]

**Example 3:**

Input: strs = ["a"]

Output: [["a"]]

**Constraints:**

1 <= strs.length <= 104

0 <= strs[i].length <= 100

strs[i] consists of lowercase English letters.


## 🧠 Key Insight

👉 Anagrams have the same character frequency

So if two strings:

"eat" → {'e':1,'a':1,'t':1}

"tea" → {'t':1,'e':1,'a':1}

Their signature is identical.

We group strings using this signature as the hash key.


## ✅ Approach 1 (Most Common – Sorting)


* Sort each string

* Use sorted string as key

* Group original strings under that key


🧾 Code (Sorting Based)
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())


## 🧪 Example Walkthrough

"eat" → "aet"

"tea" → "aet"

"ate" → "aet"

"tan" → "ant"

"nat" → "ant"

"bat" → "abt"

Groups:
"aet": ["eat","tea","ate"]
"ant": ["tan","nat"]
"abt": ["bat"]


## ⏱ Complexity

Time: O(n * k log k)

(k = max word length)

Space: O(n)


## ✅ Approach 2 (Optimized – Frequency Count) ⭐ INTERVIEW FAVORITE


* Count frequency of each letter

* Use a tuple of counts as key


🧾 Code (Frequency Based)

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())
        

## ✅ Correct Approach (HashMap + Character Count)

Step-by-step plan

**Create a hashmap**

👉 key = character frequency

👉 value = list of anagrams

**For each word:**

Count how many times each letter appears

Convert that count into a tuple

Use it as a hashmap key

Append the word to its group


## 🧩 Why tuple?

Lists cannot be dictionary keys

Tuples can (they are immutable)

count = [1, 0, 0, ..., 1]   ❌ cannot be key

tuple(count)               ✅ can be key



## 🔍 Walkthrough Example

### Input

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

---

### Step 1: Process `"eat"`

Character frequency:

```text
a:1
e:1
t:1
```

Count array:

```python
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
```

Convert to tuple (dictionary key):

```python
key = tuple(count)
```

Store:

```python
groups[key] = ["eat"]
```

---

### Step 2: Process `"tea"`

Character frequency is identical:

```text
a:1
e:1
t:1
```

The generated key is exactly the same.

Update the group:

```python
groups[key] = ["eat", "tea"]
```

---

### Step 3: Process `"ate"`

Again, the same character counts produce the same key.

Update:

```python
groups[key] = ["eat", "tea", "ate"]
```

---

### Step 4: Process `"tan"`

Character frequency:

```text
a:1
n:1
t:1
```

This creates a **different key**.

```python
groups[new_key] = ["tan"]
```

---

### Step 5: Process `"nat"`

Character frequency:

```text
a:1
n:1
t:1
```

Same key as `"tan"`.

Update:

```python
groups[new_key] = ["tan", "nat"]
```

---

### Step 6: Process `"bat"`

Character frequency:

```text
a:1
b:1
t:1
```

New unique key.

```python
groups[another_key] = ["bat"]
```

---

## 📦 Final Dictionary

```python
{
    key1: ["eat", "tea", "ate"],
    key2: ["tan", "nat"],
    key3: ["bat"]
}
```

---

## 📤 Final Output

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

> **Note:** The order of the groups or the strings inside each group does **not** matter.

---

## 💡 Why Does This Work?

Anagrams contain the **same characters with the same frequency**.

Instead of sorting every string, we create a **26-length frequency array**:

```python
count = [0] * 26
```

For each character:

```python
count[ord(char) - ord('a')] += 1
```

Finally, convert it into a tuple:

```python
key = tuple(count)
```

Since tuples are immutable and hashable, they can be used as dictionary keys.

Therefore:

```text
"eat" → (1,0,0,0,1,...,1,...)
"tea" → (1,0,0,0,1,...,1,...)
"ate" → (1,0,0,0,1,...,1,...)
```

All three generate the **same key**, so they are grouped together automatically.


## 🔁 Code Explanation

```python
groups = defaultdict(list)
```

Creates a defaultdict where the default value is an empty list [].

Purpose: We will use the frequency tuple of each word as the key, and append words to the list corresponding to that key.

Example :-

groups = {}

**If key (like a frequency tuple) is missing, it will automatically create groups[key] = []**


```python
for word in strs:**
```

Loop through each word in the input list strs.

Example:

strs = ["eat", "tea", "tan"]

word will first be "eat", then "tea", then "tan".


```python
count = [0] * 26   # for a-z
```

Creates a list of 26 zeros.

Each index corresponds to a lowercase letter:

0 → 'a', 1 → 'b', ..., 25 → 'z'.

This list will count the frequency of each letter in the current word.

* Example:

    * word = "eat"

    * count = [0, 0, 0, ..., 0]  # 26 zeros
      

```python
for ch in word:
    count[ord(ch) - ord('a')] += 1
```

Loop through each character ch in the current word.

ord(ch) gives the ASCII code of the character.

ord('a') is subtracted to get the index from 0 to 25

**3️⃣ What does ord(ch) do?**

ord() gives the ASCII number of a character.

Examples:

ord('a') = 97

ord('b') = 98

ord('e') = 101

ord('t') = 116



## 🔤 ASCII Numbers

### 1️⃣ What is ASCII?

ASCII is a standard that assigns a **number to every character**.

Think of it as:

> **Every character has its own ID number.**

| Character | ASCII Value |
|-----------|------------:|
| `'a'` | 97 |
| `'b'` | 98 |
| `'c'` | 99 |
| `'d'` | 100 |
| `'e'` | 101 |
| ... | ... |
| `'z'` | 122 |

---

### 2️⃣ Why are letters in sequence?

Lowercase letters are stored continuously.

```text
'a' = 97
'b' = 98
'c' = 99
...
'z' = 122
```

Each next letter is simply:

```text
next_letter = previous_letter + 1
```

This is why we can easily convert letters to array indices.

---

### 💡 DSA Trick

```python
index = ord(char) - ord('a')
```

Example:

```python
ord('c') - ord('a')

99 - 97

= 2
```

So:

```text
'a' → 0
'b' → 1
'c' → 2
...
'z' → 25
```

This pattern is commonly used in **Anagrams, Frequency Counting, and Sliding Window** problems.
____________________________________________________

### 3️⃣ What problem are we solving?

We want to store letter counts in a list:

count = [0] * 26

Indexes:

0 → a

1 → b

2 → c

...

25 → z

So we must convert:

'a' → 0

'b' → 1

'c' → 2


### 4️⃣ Why subtract 'a'?

Let’s see what happens:

For 'a'

ord('a') - ord('a') = 97 - 97 = 0

For 'b'

ord('b') - ord('a') = 98 - 97 = 1

For 'e'

ord('e') - ord('a') = 101 - 97 = 4

For 'z'

ord('z') - ord('a') = 122 - 97 = 25


## 📝 Example with `"eat"`

| Character | `ord(ch)` | `ord(ch) - ord('a')` | Count After Increment |
|-----------|----------:|----------------------:|----------------------|
| `e` | 101 | 4 | `count[4] = 1` |
| `a` | 97 | 0 | `count[0] = 1` |
| `t` | 116 | 19 | `count[19] = 1` |

### Final Count Array

```python
[1, 0, 0, 0, 1, 0, ..., 1, ..., 0]
```

Only these indices have a value of `1`:

```text
Index 0  → 'a'
Index 4  → 'e'
Index 19 → 't'
```


```python
groups[tuple(count)].append(word)
```

tuple(count) converts the count list to a tuple (immutable).

Tuples can be used as dictionary keys, lists cannot.

Append the current word to the list corresponding to its frequency tuple in groups.


**Example:**

```python
key = tuple([1,0,0,0,1,0,...,1,...0])
groups[key] = ["eat"]   # first word
groups[key].append("tea")  # second word, same letter frequency
groups[key].append("ate")  # third word

return list(groups.values())
```

groups.values() returns all the lists of words (all anagram groups).

Convert it to a list and return.

**Example output:**

```text
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]
```

## ⏱ Complexity

Time: O(n * k) (k = max word length)

Space: O(n)

## 🧠 When to Use Which?

| Method |  Use When |
|-----------|------------:|
| `Sorting` | Simpler, readable |
| `Frequency` | Faster, interviewer-impressing|




## 🚨 Common Mistakes

❌ Using list as dictionary key

❌ Forgetting to convert count list to tuple

❌ Sorting and storing sorted string instead of original


## 🧠 Pattern to Remember

🔑 Canonical Form / Signature Pattern

## Used in:

Group Anagrams

Valid Anagram

Isomorphic Strings

Word Pattern
