# Reverse a row in a mtrix

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

newArr = [row[::-1] for row in arr]

for i in range(len(newArr)):
    for j in range(len(newArr[i])):
        print(newArr[i][j], end=" ")
    print()

