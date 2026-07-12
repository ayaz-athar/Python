import os

folder = "tables"
os.makedirs(folder, exist_ok=True)

for table in range(2, 21):
    filename = os.path.join(folder, f"table_{table}.txt")

    with open(filename, "w") as f:
        for i in range(1, 11):
            f.write(f"{table} x {i} = {table*i}\n")

print("All tables generated successfully.")