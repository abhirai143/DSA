def add_numbers(x, y):
    while y != 0:
        temp = x & y
        x = x ^ y
        y = temp << 1
    return x
 
num1 = 10
num2 = 15
sum_result = add_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is: {sum_result}")
