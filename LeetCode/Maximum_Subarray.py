class Solution(object):
    def maxSubArray(self, nums):
        maxsum=nums[0]
        curr=0
        for i in nums:
            if curr<0:
                curr=0
            curr= curr+i
            maxsum=max(curr,maxsum)
        return maxsum
