class Solution(object):
    def addToArrayForm(self, num, k):
        str1=""
        str1 += "".join(str(i) for i in num)
        sum=str(int(str1)+k)
        l=[]
        for i in sum:
            l.append(int(i))
        return l
