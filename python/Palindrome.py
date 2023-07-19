def isPalindrome(strng):
    if len(strng) == 0:
        return 'It is a Palindrome'
    if strng[0] != strng[len(strng)-1]:
        return 'Not a Palindrome'
    return isPalindrome(strng[1:-1])
s='malayalam'
print(isPalindrome(s))