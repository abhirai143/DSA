def flatten(arr):
    res = []
    for i in arr:
        if type(i) is list:
            res.extend(flatten(i))
        else:
            res.append(i)
    return res
print(flatten([1,2,3,[4,5],6,7,[9,11,10]]))
