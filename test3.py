# 0.1*d+0.25*q = 1.3
# d+q=7

import numpy as np

A = np.array([[0.1, 0.25], [1, 1]])

B = np.array([1.3, 7])

solution = np.linalg.solve(A, B)

print(f"d: {int(solution[0])}, q: {int(solution[1])}")
