# dictionary_basics.py

# (1) Basic Dictionary and Access
dict_example = {
    "Manish": "Human being",
    "Spoon": "Object",
    456: "Integer"
}
print(dict_example["Manish"])  # Output: Human being
print(dict_example["Spoon"])   # Output: Object
print(dict_example[456])       # Output: Integer


# (2) Dictionary with Integer Keys
dict1 = {
    344: "Manish",
    234: "Harry",
    123: "Shubham"
}

print(dict1[123])  # Output: Shubham
# Here 344 is key and "Manish" is value.


# (3) Dictionary Access Methods
info = {'name': 'Karan', 'age': '19', 'eligible': True}

print(info)                  # Prints entire dictionary
print(info['name'])          # Access using key directly
print(info.get('name'))      # Access using get() method

# (4) Safe Access
# print(info['name2'])       # ❌ Error: Key doesn't exist
print(info.get('name2'))     # ✅ Output: None (safe method)

# (5) Dictionary Keys and Values
print(info.keys())           # Prints all keys
print(info.values())         # Prints all values

# (6) Access Multiple Values via Loop
print("\nAccessing values using keys:")
for key in info.keys():
    print(info[key])

print("\nAccessing values with formatted output:")
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

# (7) Access Using items() for key-value pairs
print("\nUsing items() to access key-value pairs:")
print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

    