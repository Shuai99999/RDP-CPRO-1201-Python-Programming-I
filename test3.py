# Q7
# a)
def fibonacci_recursively(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursively(n - 1) + fibonacci_recursively(n - 2)


print(fibonacci_recursively(40))
# print(fibonacci_recursively(100))


# b)
def fibonacci_loop(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci_loop(40))
print(fibonacci_loop(100))
