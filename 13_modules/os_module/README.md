# Folder Creation & Renaming Script

This script demonstrates how to use Python's `os` module to **create directories** and **rename them**.

---

## 📜 Code Explanation

```python
import os

# Step 1: Create the main folder if it doesn't exist
if (not os.path.exists("MANISHP")):
    os.mkdir("MANISHP")

# Step 2: Loop through 100 folders
for i in range(0, 100):
    # Example (commented): Create folders like Day1
