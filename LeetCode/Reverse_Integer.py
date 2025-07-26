class Solution(object):
    def reverse(self, x):
        res=0
        if x>0:
            res=int(str(x)[::-1])
        if x<0:
            res=int(("-"+str(x*-1)[::-1]))
        if res <= -2**31 or res >= 2**31:
            return 0
        else:
            return res
