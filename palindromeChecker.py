def isPalindrome(s):
    return s == s[::-1]

s = str(input())
answer = isPalindrome(s)
if answer:
    print("Yes")
else:
    print("No")