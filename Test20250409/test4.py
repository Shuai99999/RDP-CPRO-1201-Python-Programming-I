num = int(input("Please input a prime number:"))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


while not is_prime(num):
    print(f"{num} is not a prime number.")
    num = int(input("Please input a prime number:"))
print(f"Congratulations! {num} is a prime number.")

# Forgot to finish this requirement in the exam, so I will finish it now.
i = num
while i > 1:
    if i**0.5 == int(i**0.5):
        print(f"{i} is a perfect smaller square.")
        break
    i -= 1

i = num
while True:
    if i**0.5 == int(i**0.5):
        print(f"{i} is a perfect bigger square.")
        break
    i += 1
