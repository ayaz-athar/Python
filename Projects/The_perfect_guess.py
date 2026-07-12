import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

guesses = 0

print("🎮 Welcome to The Perfect Guess Game!")
print("Guess a number between 1 and 100.\n")

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess > number:
        print("⬇️ Lower number please!\n")

    elif guess < number:
        print("⬆️ Higher number please!\n")

    else:
        print(f"\n🎉 Congratulations! You guessed the correct number: {number}")
        print(f"You guessed it in {guesses} attempts.")
        break