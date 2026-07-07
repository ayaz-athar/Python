import random

choices = ["snake", "water", "gun"]

print("Snake Water Gun Game")
print("Choose: snake, water, or gun")

user = input("Enter your choice: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user not in choices:
    print("Invalid choice! Please choose snake, water, or gun.")

elif user == computer:
    print("It's a draw!")

elif user == "snake" and computer == "water":
    print("You win! Snake drinks water.")

elif user == "water" and computer == "gun":
    print("You win! Water damages gun.")

elif user == "gun" and computer == "snake":
    print("You win! Gun kills snake.")

else:
    print("You lose!")