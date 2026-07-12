with open("file1.txt") as f1:
    data1 = f1.read()

with open("file2.txt") as f2:
    data2 = f2.read()

if data1 == data2:
    print("Files are identical.")
else:
    print("Files are different.")