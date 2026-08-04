# Dota2 Senate (LeetCode 649)

The Dota2 senate consists of senators from two parties:

- **R** → Radiant
- **D** → Dire

The voting happens in **rounds**.

Each senator can perform one of two actions:

1. Ban one senator from the opposite party.
2. If all remaining senators belong to the same party, declare victory.

Every senator plays optimally for their own party.

Return:

```text
"Radiant"
```

or

```text
"Dire"
```

depending on which party wins.



## Example 1

```text
Input:

senate = "RD"

Output:

"Radiant"
```

Explanation

```text
R acts before D.

R bans D.

Only Radiant senators remain.

Radiant wins.
```



## Example 2

```text
Input:

senate = "RDD"

Output:

"Dire"
```

Explanation

```text
Round 1

R bans the first D.

Remaining active senators:

R D

↓

The second D still gets a turn.

↓

Second D bans R.

↓

Only Dire remains.

↓

Dire wins.
```



## Constraints

```text
1 <= senate.length <= 10^4

senate[i] is either 'R' or 'D'
```



# Pattern

```text
Queue

Simulation

Greedy
```



# Recognition

Use this pattern when the problem involves:

- Turns happen in order
- Multiple rounds
- Players are eliminated
- Survivors continue
- Order must be preserved



# Brute Force

## Intuition

Actually simulate every round.

Keep track of which senators are still alive.

Whenever a senator gets a turn:

- Search for the next available opponent.
- Ban that opponent.
- Continue until only one party remains.



## Algorithm

1. Store all senators.
2. Traverse one by one.
3. Find the nearest opponent.
4. Ban them.
5. Continue round after round.
6. Stop when only one party remains.



## Why is it Slow?

Each senator may have to search almost the entire array to find an opponent.

Since multiple rounds occur, this becomes expensive.



## Complexity

```text
Time : O(n²)

Space : O(n)
```



# Optimal Approach (Two Queues)

## Key Observation

Instead of storing characters,

store **their indices**.

Example

```text
R D R R

0 1 2 3
```

Queues become

```text
Radiant

[0,2,3]

Dire

[1]
```

The senator with the **smaller index gets to act first.**



# Why Compare Indices?

Suppose

```text
Radiant = 2

Dire = 5
```

Timeline

```text
2 ---------- 5

R            D
```

Radiant reaches the microphone first.

Radiant bans Dire.

---

Suppose

```text
Radiant = 8

Dire = 6
```

Timeline

```text
6 ---------- 8

D            R
```

Dire reaches first.

Dire bans Radiant.

Therefore

```python
if r < d:
```

means

```text
Did Radiant get their turn before Dire?
```

If yes,

Radiant survives.

Otherwise,

Dire survives.



# Why Do We Add `index + n`?

Suppose

```text
senate = "RDR"

Length = 3
```

Timeline

```text
Round 1

0    1    2

R₁   D   R₂
```

If the Radiant at index **0** survives,

he has already used his turn.

His next turn should come **after everyone else finishes**.

So

```python
0 + 3 = 3
```

Timeline becomes

```text
0    1    2    3

R₁   D   R₂   R₁
```

Notice

The last **R₁** is **NOT** a new senator.

It is the **same senator** getting another turn.

Think of the numbers as **timestamps**, not original indices.



# Intuition

Create two queues.

One stores Radiant indices.

One stores Dire indices.

Each round:

- Pop one Radiant.
- Pop one Dire.
- Compare indices.
- Smaller index acts first.
- Larger index is banned.
- Winner is added back using

```python
index + n
```

because their next turn is in the next round.

Repeat until one queue becomes empty.



# Algorithm

1. Create two queues.
2. Traverse the string.

   - Push Radiant indices into the Radiant queue.
   - Push Dire indices into the Dire queue.

3. While both queues are non-empty:

   - Pop one index from each queue.
   - Compare them.
   - Smaller index wins.
   - Push the winner back with `index + n`.

4. If Radiant queue remains,

```text
Return "Radiant"
```

Else

```text
Return "Dire"
```



# Code

```python
from collections import deque

class Solution(object):

    def predictPartyVictory(self, senate):

        n = len(senate)

        radiant = deque()
        dire = deque()

        for i, ch in enumerate(senate):

            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            if r < d:

                radiant.append(r + n)

            else:

                dire.append(d + n)

        if radiant:
            return "Radiant"

        return "Dire"
```



# Walkthrough

## Example

```text
senate = "RDD"
```

Length

```text
n = 3
```

Initial queues

```text
Radiant

[0]

Dire

[1,2]
```



## Iteration 1

Pop

```text
r = 0

d = 1
```

Compare

```text
0 < 1
```

Radiant acts first.

Radiant bans Dire.

Radiant survives.

Push back

```python
0 + 3 = 3
```

Queues become

```text
Radiant

[3]

Dire

[2]
```



## Iteration 2

Pop

```text
r = 3

d = 2
```

Compare

```text
3 < 2

False
```

Dire acts first.

Dire bans Radiant.

Dire survives.

Push back

```python
2 + 3 = 5
```

Queues become

```text
Radiant

[]

Dire

[5]
```

Radiant queue is empty.

Return

```text
"Dire"
```



# Dry Run

| Radiant Queue | Dire Queue | Compare | Winner | New Queues |
|--------------|-----------|---------|--------|-----------|
| [0] | [1,2] | 0 < 1 | Radiant | R:[3] D:[2] |
| [3] | [2] | 3 < 2 | Dire | R:[] D:[5] |



# Complexity

```text
Time : O(n)
```

Every senator is inserted and removed from a queue only a limited number of times.

```text
Space : O(n)
```

For storing the two queues.



# Common Mistakes

### ❌ Comparing characters instead of indices

Wrong

```python
if senate[r] == "R":
```

The decision depends on **who gets the turn first**, not the character.



### ❌ Appending both senators

Wrong

```python
radiant.append(r+n)
dire.append(d+n)
```

Only the **winner** survives.

The loser is permanently banned.



### ❌ Forgetting `+ n`

Wrong

```python
radiant.append(r)
```

The surviving senator has already taken their turn.

They must wait until the next round.



### ❌ Thinking `r + n` creates a new senator

It does **not**.

```text
0

↓

4

↓

8

↓

12
```

This is the **same senator** getting future turns.

The values become **timestamps**, not original indices.



### ❌ Confusing

```python
while radiant and dire:
```

with comparing queues.

It simply means

```python
while len(radiant) > 0 and len(dire) > 0:
```

Fight continues while **both parties still have senators**.



# Similar Problems

- Number of Recent Calls
- Design Circular Queue
- Task Scheduler
- Josephus Problem
- Rotting Oranges (Simulation)



# Interview Takeaway

## Recognition

```text
Queue

Simulation

Round-Based Processing

Greedy

Turn Order
```

## Core Trick

```text
Store Indices

↓

Smaller Index Acts First

↓

Winner Survives

↓

Winner Goes To Next Round

↓

Append index + n

↓

Repeat Until One Queue Is Empty
```
