#Sometimes a programmer wants to execute a group of statments a certian number of times .this can be done using loops.
#for loop:- for loops can iterate over a sequence is nothing but iterating over strings,lists,tuples,sets and dictionaries
# For Loops in Python

##  Definition:
A `for` loop in Python is used to iterate over a sequence (like list, tuple, string, or `range()`).

---

##  Basic Syntax
```python
for variable in iterable:
    # block of code

#  While Loops in Python

This folder contains examples of using `while` loops in Python, including a simulation of a `do-while` loop.

---

##  What You'll Learn
- How `while` loops work
- Loop execution based on a condition
- Simulating a `do-while` loop using `while True` and `break`

---

##  Basic Syntax
```python
while condition:
    # code block
# For-Else and While-Else in Python

# What is `else` in loops?

In Python, the `else` block after a `for` or `while` loop runs **only when the loop finishes normally**.

> If the loop is **not interrupted by a `break`**, then the `else` part runs.

---

##  For Loop with Else

```python
for i in range(5):
    print(i)
else:
    print("Loop finished without break")
