def isPalindrome(s):
    res=""
    for ch in s:
        if ch.isalnum():
            res+=ch.lower()
    if res==res[::-1]:
        return True
    else:
        return False
    
s="A man, a plan, a canal: Panama"
palindrome=isPalindrome(s)
print(palindrome)
