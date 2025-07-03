# For-Else and While-Else in Python

# What is `else` in loops?

In Python, the `else` block after a `for` or `while` loop runs **only when the loop finishes normally**.

> If the loop is **not interrupted by a `break`**, then the `else` part runs.

---

## 🔁 For Loop with Else

```python
for i in range(5):
    print(i)
else:
    print("Loop finished without break")
