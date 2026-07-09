with open("poems.txt", "r") as f:
    content = f.read().lower()

if "twinkle" in content:
    print("Twinkle is present")
else:
    print("Twinkle is not present")