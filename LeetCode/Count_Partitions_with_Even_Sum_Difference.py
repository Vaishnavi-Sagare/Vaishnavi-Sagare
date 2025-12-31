class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt=0
        i=0
        while i<len(nums)-1:
            a=nums[:i+1]
            b=nums[i+1:]
            if (sum(a)-sum(b)) %2==0:
                cnt += 1
            i += 1
        return cnt
