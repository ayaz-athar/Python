files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f"\nContents of {file}:")
            print(f.read())
    except FileNotFoundError:
        print(f"{file} is not present.")