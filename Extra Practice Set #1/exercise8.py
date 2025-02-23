import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
print(num1, num2)

for num in range(num1, num2 + 1):
    # Skip numbers less than 2, as they are not prime
    if num < 2:
        continue

    # Assume the number is prime
    is_prime = True

    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # If it's prime, print the number
    if is_prime:
        print(num)
