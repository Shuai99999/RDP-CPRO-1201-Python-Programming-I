def is_prime(num):
    if num < 1:
        print("Please input a number > 1")
        return False

    if num % 1 != 0:
        print("Please input an integer")
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        return True


print(is_prime(53))
