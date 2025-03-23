def find_max(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num


print(find_max([200, 15, 22, 0, -3000, -29, 2005]))
