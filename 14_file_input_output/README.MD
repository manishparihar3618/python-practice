print(f) → shows the file object info (<_io.TextIOWrapper ...>).
This doesn’t show file contents, just metadata (name, mode, encoding).

text = f.read() → reads the whole content of myfile.txt into a string.

print(text) → displays the actual content of the file.
In your case, the file has:
 Hey manish  

f.close() → properly closes the file


# Read Mode (r):-Default mode in Python (open("file.txt") is the same as open("file.txt", "r")).

Used to read the contents of a file.

File must exist → otherwise it raises FileNotFoundError.

The file pointer (cursor) starts at the beginning of the file.
# Write Mode (w)
Opens the file for writing.

If the file does not exist, Python will create it.

If the file already exists, its content will be erased (overwritten).

File pointer is placed at the beginning before writing.




# Append Mode (a)
Opens the file for adding new content at the end.

If the file does not exist, Python will create it.

Existing content is not deleted.

File pointer is placed at the end of the file before writing.



# Create Mode





# Text Mode





# Binary Mode




# rt



# rb




# Common modes:
# 'r'  → Read (default) - error if file doesn’t exist
# 'w'  → Write - creates new file / overwrites existing
# 'a'  → Append - creates new file / adds at the end if exists
# 'x'  → Create - creates new file, error if file already exists

# 't'  → Text mode (default)
# 'b'  → Binary mode (for images, PDFs, etc.)
