word = "Donkey"

with open("sample.txt", "r") as f:
    content = f.read()

content = content.replace(word, "#####")

with open("sample.txt", "w") as f:
    f.write(content)

print("Word replaced successfully.")