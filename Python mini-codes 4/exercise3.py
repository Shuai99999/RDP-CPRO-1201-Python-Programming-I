import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Guess the number (between 1 and 100). You have 3 attempts!")

# Allow the user to guess three times
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed the correct number!")
        break  # Exit the loop since the user guessed correctly
    elif guess < secret_number and attempt < 3:
        print("🔼 Too low! Try a higher number.")
    elif guess > secret_number and attempt < 3:
        print("🔽 Too high! Try a lower number.")
    else:
        print(f"❌ Sorry, the correct number was {secret_number}. Keep practicing!")
