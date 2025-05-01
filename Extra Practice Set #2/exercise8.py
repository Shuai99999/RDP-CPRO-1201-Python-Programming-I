import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
# print(num1, num2)

for num in range(num1, num2 + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
