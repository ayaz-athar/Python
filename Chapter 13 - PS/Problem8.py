with open("log.txt") as f:
    lines = f.readlines()

for index, line in enumerate(lines, start=1):
    if "python" in line.lower():
        print("Python found at line", index)
        break
else:
    print("Python not found.")