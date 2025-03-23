def filter_odds(nums):
    return [num for num in nums if num % 2 != 0]


print(filter_odds([2, 4, 3, 6, 8, 1]))
