def count_occurrences(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count


print(count_occurrences([1, 2, 3, 2, 4, 2, 5], 2))
