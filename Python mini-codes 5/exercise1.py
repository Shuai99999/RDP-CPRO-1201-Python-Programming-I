import random

number_to_guess = random.randint(1, 100)
max_guesses = 6

for guesses_left in range(max_guesses, 0, -1):
    user_guess = int(
        input(
            f"Guess the number between 1 and 100. You have {guesses_left} guesses left: "
        )
    )

    if user_guess == number_to_guess:
        print("Congrats! You WON")
        break
    else:
        if user_guess < number_to_guess:
            print(
                f"Try again! You have {guesses_left - 1} more choices. The number is higher than your previous guess."
            )
        else:
            print(
                f"Try again! You have {guesses_left - 1} more choices. The number is lower than your previous guess."
            )

if guesses_left == 1:
    print("You lost!")
