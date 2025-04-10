def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)


print(power(2, 3))
print(power(3, 4))
