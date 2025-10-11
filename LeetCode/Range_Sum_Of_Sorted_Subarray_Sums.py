class Solution(object):
    def rangeSum(self, nums, n, left, right):
        x=[]
        for i in range(n):
            x.append(nums[i])
            sum=nums[i]
            for j in range(i+1,n):
                sum += nums[j]
                x.append(sum)
        x.sort()
        res=0
        for i in range(left-1,right):
            res = (res + x[i])%((10**9)+7)
        return res
