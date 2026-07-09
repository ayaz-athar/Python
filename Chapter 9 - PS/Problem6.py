with open("log.txt", "r") as f:
    content = f.read().lower()

if "python" in content:
    print("Python is present")
else:
    print("Python is not present")