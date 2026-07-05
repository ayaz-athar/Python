# 5. Name present in list
names = ["ayaz", "ali", "rahul", "harry", "aman"]

name = input("Enter name: ")

if name.lower() in names:
    print("Name is present in the list")
else:
    print("Name is not present in the list")