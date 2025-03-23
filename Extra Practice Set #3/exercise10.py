def factorial(n):
    if n < 0:
        return "Please input a non-negative number."
    if n == 0:
        return 0

    result = 1

    while n > 1:
        result *= n
        n -= 1
    return result


print(factorial(9))
print(factorial(0))
