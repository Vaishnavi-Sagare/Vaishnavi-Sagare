class Solution(object):
    def romanToInt(self, s):
        res=0
        l1={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s)>=1 and len(s)<=15:
            for i in range(len(s)):
                if i+1 < len(s) and l1[s[i]]<l1[s[i+1]]:
                    res -= l1[s[i]]
                else:
                    res += l1[s[i]]
        return res
