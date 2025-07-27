lass Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x>=-2**31 and x<= (2**31)-1:
            y=int(str(x)[::-1])
            if x==y:
                return True
        return False
