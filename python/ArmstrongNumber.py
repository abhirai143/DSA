import math as m

def getSum(num, num_length):
    if num == 0:
        return num
    else:
        return m.pow((num % 10), num_length) + getSum(num//10, num_length)

# get input from user
num = int(input("Enter a number: "))

# get input number length
num_length = len(str(num))
sum = getSum(num, num_length)

# display output
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
