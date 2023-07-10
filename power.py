def power(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power(num, topwr - 1)


print('{} to the power of {} is {}'.format(4, 7, power(4, 7)))
print('{} to the power of {} is {}'.format(2, 8, power(2, 8)))
