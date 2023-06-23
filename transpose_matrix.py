import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(arr)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        result[j][i] = arr[i][j]

for r in result:
    print(r)
