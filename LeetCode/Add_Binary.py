class Solution(object):
    def addBinary(self, a, b):
        a,b=int(a,2),int(b,2)
        sum=a+b
        return (str(bin(sum))[2:])
