def square_of_odds(nums):
    return [x**2 for x in nums if x % 2 != 0]


print(square_of_odds([1, 2, 3, 4, 5]))
