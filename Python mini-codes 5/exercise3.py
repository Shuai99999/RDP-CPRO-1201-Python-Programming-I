import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

if num1 > num2:
    num1, num2 = num2, num1

prime_numbers = []

for num in range(num1, num2 + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)

print(f"The prime numbers between {num1} and {num2} are: {prime_numbers}")
