import numpy as np

array = np.array([1, 2, 6, 3, 14, 9, 13, 10])


def max(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > max:
                max = arr[i] * arr[j]
                pairs = str(arr[i]) + "," + str(arr[j])
    print(pairs)
    print(max)


max(array)
