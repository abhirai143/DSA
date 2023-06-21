a = [1, 2, 3]
b = [2, 1, 3]


def permutation(x, y):
    if len(a) != len(b):
        return False
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False


print(permutation(a, b))
