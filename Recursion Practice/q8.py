
# check if the string is palindrome or not

def palindrome(s):

    l = len(s)

    for i in range(l):
        if s[i] != s[l-1-i]:
            return False
    
    return True

# s = "ABCDCBA"
s = "ABCD"
print(palindrome(s))