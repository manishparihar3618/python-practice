# Python Module Import Example

This project demonstrates how to **import functions from another Python file (module)** and use them in the main script.

---

##  Project
---

## ⚙️ How It Works
1. **`math_utils.py`**
   - Defines a function `add(a, b)` to return the sum of two numbers.
   - When the file is imported, it prints:
     ```
     math_utils.py file is being loaded...
     ```
   - If run directly, it executes the code inside:
     ```python
     if __name__ == "__main__":
         print("math_utils.py is being run directly")
         x, y = 5, 3
         print("Addition:", add(x, y))
     ```

2. **`main.py`**
   - Imports `math_utils`.
   - Calls the function `math_utils.add(10, 20)` and prints the result.

---

## ▶️ Running the Code

### Run `main.py`
```bash
python main.py
