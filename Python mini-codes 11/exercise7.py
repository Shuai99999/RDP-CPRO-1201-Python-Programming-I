import numpy as np

nums = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

second_row = nums[1]
print(second_row)

gt_6 = nums[nums > 6]
print(gt_6)

nums_dbl = nums * 2
print(nums_dbl)

nums[:, 2] = nums[:, 2] + 1
print(nums)
