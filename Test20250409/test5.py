num = int(input("Please input a number:"))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(f"The prime factors of {num} are:")
for i in range(2, num):
    if num % i == 0:
        if is_prime(i):
            print(i)
