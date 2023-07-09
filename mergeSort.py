import math

def mergeSort(items):
    print('mergeSort() called on:', items)

    if len(items) == 0 or len(items) == 1:
        return items

    iMiddle = math.floor(len(items) / 2)

    print('................Split into:', items[:iMiddle], 'and', items[iMiddle:])

    left = mergeSort(items[:iMiddle])
    right = mergeSort(items[iMiddle:])

    sortedResult = []
    iLeft = 0
    iRight = 0
    while (len(sortedResult) < len(items)):
        if left[iLeft] < right[iRight]:
            sortedResult.append(left[iLeft])
            iLeft += 1
        else:
            sortedResult.append(right[iRight])
            iRight += 1

        if iLeft == len(left):
            sortedResult.extend(right[iRight:])
            break
        elif iRight == len(right):
            sortedResult.extend(left[iLeft:])
            break

    print('The two halves merged into:', sortedResult)

    return sortedResult 
myList = [0, 7, 6, 3, 1, 2, 5, 4]
myList = mergeSort(myList)
print(myList)
