# Number of Recent Calls (LeetCode 933)

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t` (in milliseconds) and returns the number of requests that happened in the past **3000 milliseconds**, including the current request.

Specifically, count all requests in the range:

```text
[t - 3000, t]
```

It is guaranteed that every call to `ping()` uses a strictly larger value of `t` than the previous call.



**Example**

Input

```text
["RecentCounter","ping","ping","ping","ping"]

[[],[1],[100],[3001],[3002]]
```

Output

```text
[null,1,2,3,3]
```

Explanation

```text
ping(1)

Window

[-2999,1]

Requests

[1]

Answer = 1
```

```text
ping(100)

Window

[-2900,100]

Requests

[1,100]

Answer = 2
```

```text
ping(3001)

Window

[1,3001]

Requests

[1,100,3001]

Answer = 3
```

```text
ping(3002)

Window

[2,3002]

Requests

[1,100,3001,3002]

1 is outside the window

Remaining

[100,3001,3002]

Answer = 3
```



**Constraints**

```text
1 <= t <= 10^9

t is strictly increasing.

At most 10^4 calls.
```

---

# Pattern

**Queue (Deque) + Sliding Window**

---

# Recognition

Use this pattern when the question contains:

- Recent requests
- Last K seconds / milliseconds
- Streaming data
- Moving time window
- Remove oldest data first

---

# Key Observation

The problem only cares about requests that happened in the last **3000 milliseconds**.

If the current request arrives at time:

```text
t
```

Then the valid window is

```text
[t-3000, t]
```

Any request before

```text
t-3000
```

is too old and should be removed.

---

# Intuition

Imagine people entering a building.

The guard only wants people who entered in the **last 3000 milliseconds**.

Whenever a new person enters:

1. Add them to the queue.
2. Remove everyone who entered before the allowed window.
3. Count the remaining people.

Since requests always arrive in increasing order, the oldest request is always at the front of the queue.

---

# Algorithm

1. Create an empty queue.
2. Whenever `ping(t)` is called:
   - Add `t` to the queue.
3. While the oldest request is outside the window:
   - Remove it.
4. Return the size of the queue.

---

# Code

```python
from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):

        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
```

---

# Why do we check?

```python
while self.q[0] < t - 3000:
```

Suppose

```text
Current Time = 7000
```

Then the valid window is

```text
7000 - 3000 = 4000

Window

[4000,7000]
```

Queue

```text
[2000,3500,4500,5000,7000]
```

Check the oldest request.

```text
2000 < 4000

YES
```

It happened **before the window started**, so remove it.

Queue

```text
[3500,4500,5000,7000]
```

Again

```text
3500 < 4000

YES
```

Remove it.

Queue

```text
[4500,5000,7000]
```

Again

```text
4500 < 4000

NO
```

Stop.

Now every request is inside

```text
[4000,7000]
```

---

# Walkthrough

### Example

```text
ping(3002)
```

Queue before

```text
[1,100,3001]
```

Add current request

```text
[1,100,3001,3002]
```

Window

```text
3002 - 3000 = 2

[2,3002]
```

Check oldest

```text
1 < 2

YES
```

Remove it.

Queue

```text
[100,3001,3002]
```

Check again

```text
100 < 2

NO
```

Return

```text
3
```

---

# Dry Run

| Queue Before | Current Time | Window | Remove? | Queue After | Answer |
| ------------ | ------------ | ------ | ------- | ----------- | ------ |
| [1] | 1 | [-2999,1] | No | [1] | 1 |
| [1,100] | 100 | [-2900,100] | No | [1,100] | 2 |
| [1,100,3001] | 3001 | [1,3001] | No | [1,100,3001] | 3 |
| [1,100,3001,3002] | 3002 | [2,3002] | Remove 1 | [100,3001,3002] | 3 |

---

# Edge Cases

```text
Only one request

ping(1)

Output

1
```

---

```text
All requests are recent

[100,500,1000]

Nothing gets removed.
```

---

```text
Multiple old requests

Queue

[100,500,1000,4500]

Current Time

5000

Window

[2000,5000]

Remove

100

500

1000

Keep

4500
```

---

# Complexity

```text
Time  : O(n)
```

Although there is a `while` loop, each request is:

- Added once
- Removed once

So the total work is linear.

```text
Space : O(n)
```

where

```text
n = number of requests stored in the queue
```

---

# Common Mistakes

❌ Using `<=`

```python
while self.q[0] <= t-3000
```

The problem says

```text
[t-3000, t]
```

The range is **inclusive**, so a request exactly at `t-3000` should **not** be removed.

---

❌ Using a normal list

```python
pop(0)
```

This is **O(n)**.

Use

```python
deque()
```

because

```python
popleft()
```

is **O(1)**.

---

❌ Forgetting to add the current request first.

```python
self.q.append(t)
```

The current request must also be counted.

---

# Similar Problems

- Sliding Window Maximum
- Maximum Number of Vowels in a Substring
- Max Consecutive Ones III
- Moving Average from Data Stream

---

# Interview Takeaway

### Recognition

```text
Queue

Deque

Sliding Window

Streaming Data

Recent Requests
```

### Core Trick

```text
New Request Arrives

↓

Add to Queue

↓

Window = [t-3000, t]

↓

Remove every request older than t-3000

↓

Remaining queue size = Answer
```


# Brute Force

## Idea

Store every request in a list.

Whenever `ping(t)` is called:

- Add the new request.
- Traverse the entire list.
- Count how many requests lie in the range:

```text
[t-3000, t]
```

Return that count.

---

## Algorithm

1. Store every request in a list.
2. For every `ping(t)`:
   - Append `t`.
   - Initialize `count = 0`.
   - Traverse every request.
   - If the request lies between `t-3000` and `t`, increment `count`.
3. Return `count`.

---

## Code

```python
class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):

        self.requests.append(t)

        count = 0

        for time in self.requests:

            if t - 3000 <= time <= t:
                count += 1

        return count
```

---

## Dry Run

Requests received

```text
[1,100,3001,3002]
```

Current request

```text
t = 3002
```

Window

```text
[2,3002]
```

Traverse every request

```text
1

1 < 2

Ignore
```

```text
100

Inside Window

Count = 1
```

```text
3001

Inside Window

Count = 2
```

```text
3002

Inside Window

Count = 3
```

Return

```text
3
```

---

## Why is it Slow?

For every new request, we scan the **entire list**, even though many old requests will never be useful again.

If there are `n` requests:

- First `ping()` checks `1` element.
- Second checks `2`.
- Third checks `3`.
- ...
- Last checks `n`.

Total work:

```text
1 + 2 + 3 + ... + n

= O(n²)
```

---

## Complexity

```text
Time  : O(n) per ping
```

For `n` calls:

```text
Total Time : O(n²)
```

```text
Space : O(n)
```

---

## Optimization

Instead of checking every request every time:

- Keep only the requests inside the last 3000 milliseconds.
- Remove old requests immediately using a **Queue (Deque)**.

This reduces the overall complexity to **O(n)** for all calls.
