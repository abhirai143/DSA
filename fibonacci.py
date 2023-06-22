def allfib(n):
    for i in range(n):
        print(f"{i}, {fib(i)}")


def fib(n):
    if n < 0:
        print("INVALID INPUT!. Enter the positive integer")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-1)


n = int(input("Enter length of Fibonacci series: "))

allfib(n)
