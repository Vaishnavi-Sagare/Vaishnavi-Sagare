class Solution(object):
    def lengthOfLastWord(self, s):
        a=0
        l=s.split(" ")
        for i in l:
            if len(i)>a:
                b=len(i)
        return b
