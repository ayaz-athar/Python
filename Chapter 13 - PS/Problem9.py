with open("source.txt") as f:
    content = f.read()

with open("destination.txt", "w") as f:
    f.write(content)

print("File copied successfully.")