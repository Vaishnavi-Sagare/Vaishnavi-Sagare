class Solution(object):
    def containsDuplicate(self, nums):
        l=set()
        for num in nums:
            if num in l:
                return True
            l.add(num)
        return False
