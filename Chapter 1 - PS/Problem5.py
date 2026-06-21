import os

# Directory path
path = "."

# Get contents of directory
contents = os.listdir(path)

# Print contents
print("Contents of directory:")
for item in contents:
    print(item)