#  Python Exception Handling (Basics)

Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. In Python, exception handling prevents the program from crashing and allows it to handle errors gracefully.

## 🔸 What are Exceptions in Python?

Python has many built-in exceptions that are raised when your program encounters an error (e.g., dividing by zero, invalid input, accessing an out-of-range list index).

When such exceptions occur:
- The Python interpreter stops the current process.
- If not handled using `try...except`, the program crashes.
- Using `try...except`, we can catch and handle these errors safely.

---

## 🔹 `try...except` Syntax

```python
try:
    # Code that may raise an exception
except SomeException:
    # Code that runs if the exception occurs
