with open("log.txt", "r") as f:
    lines = f.readlines()

line_no = 1

for line in lines:
    if "python" in line.lower():
        print("Python is present on line", line_no)
        break
    line_no += 1
else:
    print("Python is not present")