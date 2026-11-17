def isPalindrome(x):
        tot=0
        temp=x
        while x>0:
            rem=x%10
            tot=tot*10+rem
            x//=10
        if temp==tot:
            return True
        else:
            return False
print(isPalindrome(1223221))