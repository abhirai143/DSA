# Linear Searhing

import numpy as np
a=np.array=([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

def search(array,number):
    for i in range(len(array)):
        if array[i] == number:
            print(f" Found at {i}th index")
search(a,1)


# Time complexity = O(n)
# Space complexity = O(1)