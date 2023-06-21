num = 5

def Factorial(n):
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * Factorial(n-1)

print(Factorial(num))