num = int(input("Enter a number: "))

table = [num * i for i in range(1, 11)]

with open("Tables.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{num} x {i} = {num*i}\n")

print("Table saved successfully.")