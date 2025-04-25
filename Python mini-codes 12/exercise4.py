def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_list = [x for x in range(1, 100) if is_prime(x) or x == 1]
print(prime_list)
