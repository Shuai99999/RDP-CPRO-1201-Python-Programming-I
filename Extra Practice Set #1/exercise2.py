import random

random_number = random.randint(1, 100)
# print(random_number)
guess_time = 1
isSuccess = False

while not isSuccess:
    user_guess = int(input(f"Guess the number, this is your {guess_time}th try: "))
    if user_guess == random_number:
        print("You win!")
        isSuccess = True
    else:
        print(f"You have tried {guess_time} times.")
    guess_time += 1
