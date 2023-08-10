decimal = temp = int(input("Please Enter a decimal number: "))
binary = ""
while temp > 0:
    remainder = temp % 2
    binary = str(remainder) + binary
    temp = temp // 2
print("Binary number is ", binary, " for ", decimal)
