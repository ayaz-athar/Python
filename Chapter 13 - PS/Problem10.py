with open("file1.txt") as f1:
    with open("file2.txt") as f2:
        if f1.read() == f2.read():
            print("Yes, both files are identical.")
        else:
            print("No, files are different.")