import random

def game():
    return random.randint(1, 100)

score = game()

with open("Hi-score.txt", "r") as f:
    hiscore = f.read()

if hiscore == "":
    hiscore = 0
else:
    hiscore = int(hiscore)

if score > hiscore:
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))

print("Your score:", score)
print("High score:", max(score, hiscore))