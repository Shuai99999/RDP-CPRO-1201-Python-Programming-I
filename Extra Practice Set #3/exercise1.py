def sum_of_evens(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum += i
    return sum


print(sum_of_evens(-8))
