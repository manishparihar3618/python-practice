# Read in text mode
f = open('myfile15.txt', 'rt')
text = f.read()
print("Reading in text mode:\n", text)
f.close()

# Example: Read in binary mode
f = open('myfile15.txt', 'rb')
text = f.read()
print("Reading in binary mode:\n", text)
f.close()