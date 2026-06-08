# Python Built-in Data Structures

Python provides four primary built-in data structures:

* **List**
* **Tuple**
* **Set**
* **Dictionary**

They differ mainly in:

* **Mutability** (whether they can be modified after creation)
* **Ordering**
* **Handling of duplicate elements**
* **Access methods (indexing or keys)**

---

## Comparison Table

| Feature                | List          | Tuple         | Set             | Dictionary          |
| ---------------------- | ------------- | ------------- | --------------- | ------------------- |
| **Syntax**             | `[]`          | `()`          | `{}` or `set()` | `{key: value}`      |
| **Ordered**            | ✅ Yes         | ✅ Yes         | ❌ No            | ✅ Yes (Python 3.7+) |
| **Mutable**            | ✅ Yes         | ❌ No          | ✅ Yes           | ✅ Yes               |
| **Duplicates Allowed** | ✅ Yes         | ✅ Yes         | ❌ No            | Keys ❌, Values ✅    |
| **Indexing**           | Integer-based | Integer-based | Not Supported   | Key-based           |

---

# 1. List

A **list** is an ordered and mutable collection of items.

Since lists are mutable, you can:

* Add elements
* Remove elements
* Modify existing elements

## Syntax

```python
shopping_list = ["apple", "banana", "cherry"]
```

## Example

```python
shopping_list = ["apple", "banana", "cherry"]

shopping_list.append("orange")

print(shopping_list)
```

### Output

```python
['apple', 'banana', 'cherry', 'orange']
```

## Common Use Cases

* Shopping carts
* User input history
* Task lists
* Storing collections where order matters

---

# 2. Tuple

A **tuple** is an ordered but immutable collection of items.

Once created, a tuple cannot be modified.

## Syntax

```python
coordinates = (10.0, 20.0)
```

## Example

```python
coordinates = (10.0, 20.0)

print(coordinates[0])
```

### Output

```python
10.0
```

## Common Use Cases

* Geographic coordinates
* Fixed configuration values
* Returning multiple values from functions
* Dictionary keys (because tuples are immutable)

---

# 3. Set

A **set** is an unordered collection of unique elements.

Sets automatically remove duplicates.

## Syntax

```python
unique_colors = {"red", "green", "blue"}
```

or

```python
unique_colors = set()
```

## Example

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

### Output

```python
{1, 2, 3, 4}
```

## Common Use Cases

* Removing duplicates
* Fast membership checking
* Mathematical set operations

### Membership Check

```python
colors = {"red", "green", "blue"}

print("red" in colors)
```

### Output

```python
True
```

---

# 4. Dictionary

A **dictionary** stores data as key-value pairs.

Each key is unique and maps to a specific value.

## Syntax

```python
user_profile = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

## Example

```python
user_profile = {
    "name": "Alice",
    "age": 30
}

print(user_profile["name"])
```

### Output

```python
Alice
```

## Common Use Cases

* User profiles
* Configuration settings
* API responses
* Frequency counting
* Lookup tables

### Accessing Values

```python
user_profile["name"]
```

### Adding a New Key

```python
user_profile["city"] = "New York"
```

---

# Quick Summary

## Use a List When

* Order matters
* Data changes frequently
* Duplicates are allowed

```python
tasks = ["Study", "Exercise", "Read"]
```

---

## Use a Tuple When

* Data should not change
* You need an immutable collection

```python
coordinates = (10.0, 20.0)
```

---

## Use a Set When

* You need unique elements
* Fast lookups are important

```python
unique_numbers = {1, 2, 3}
```

---

## Use a Dictionary When

* Data is stored as key-value pairs
* Fast retrieval by key is needed

```python
student = {
    "name": "John",
    "grade": "A"
}
```

---

# Interview Tip

A common question is:

**Which data structure should I use?**

| Requirement          | Best Choice |
| -------------------- | ----------- |
| Ordered collection   | List        |
| Immutable collection | Tuple       |
| Unique elements      | Set         |
| Key-value mapping    | Dictionary  |

Understanding when to use each data structure is more important than memorizing their definitions.
