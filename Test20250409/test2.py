num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))

if num1 < 0 or num2 < 0:
    print("Please input positive integers.")
    exit()

if num1 == num2:
    print("Please input two different integers.")
    exit()


if num1 > num2:
    num1, num2 = num2, num1


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


res = []
for num in range(num1, num2 + 1):
    if is_prime(num):
        res.append(num)

if len(res) == 0:
    print("No prime numbers found.")
else:
    print(f"Prime numbers between {num1} and {num2} are: {res}")
