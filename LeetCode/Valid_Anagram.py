class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            l=[]
            l1=[]
            for i in s:
                l.append(i)
            for i in t:
                if i not in s:
                    return False
                else:
                    l1.append(i)
            if sorted(l) == sorted(l1):
                return True
            return False
