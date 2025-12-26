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


## Types of Error in Python we can raise,
(1) ValueError in Python happens when:
👉 The type of data is correct, but its value is not appropriate for the operation.
num = int("123")   # ✅ works, "123" is a valid integer string
num = int("abcd")  # ❌ raises ValueError

(2)🔹 1. SyntaxError
Happens when your code is written incorrectly (Python can’t even run it).

print("Hello"   # ❌ missing closing parenthesis

(3)NameError
Using a variable or function that hasn’t been defined.
print(x)   # ❌ x is not defined