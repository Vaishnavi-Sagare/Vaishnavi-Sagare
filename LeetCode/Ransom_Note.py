class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        l1=list(ransomNote)
        l2=list(magazine)
        for i in l1:
            if i in l2:
                l2.remove(i)
            else:
                return False
        return True
