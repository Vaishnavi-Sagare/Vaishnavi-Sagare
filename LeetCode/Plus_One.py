class Solution(object):
    def plusOne(self, digits):
        s=''
        for i in digits:
            s += str(i)
        s=str(int(s)+1)
        l=[]
        for i in s:
            l.append(int(i))
        return l
