# While Loops in Python

### 📘 Definition:
A `while` loop executes a block of code **as long as the condition is `True`**. When the condition becomes `False`, the loop stops.

---

## ✅ Syntax:
```python
while condition:
    # Code to run while the condition is true

---

## 🔁 Simulating a Do-While Loop in Python

### ❓ What is a do-while loop?

A `do-while` loop:
- Executes the block **at least once**
- Then checks the condition to decide whether to continue

Python does **not** have a built-in `do-while` loop, but you can simulate it using `while True` and a `break`.

---

### ✅ Example:
```python
i = 0
while True:
    print(i)
    i += 1
    if i % 100 == 0:
        break
