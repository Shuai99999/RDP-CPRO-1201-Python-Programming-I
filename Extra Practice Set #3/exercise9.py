def filter_negatives(nums):
    return [num for num in nums if num >= 0]


print(filter_negatives([-1, -2, -3, 4, 5]))
