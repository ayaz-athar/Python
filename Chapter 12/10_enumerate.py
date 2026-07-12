l=[1, 2, 3, 4, 5]
index=0
for item in l:
    print(f"The item number {index} is {item}")
    index += 1

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")