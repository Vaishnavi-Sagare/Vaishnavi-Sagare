class Solution(object):
    def countHillValley(self, nums):
        ans=0
        cleaned = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                cleaned.append(nums[i])
        for i in range(1,len(cleaned)-1):
            if (cleaned[i]>cleaned[i-1]and cleaned[i]>cleaned[i+1]) or (cleaned[i]<cleaned[i-1]and cleaned[i]<cleaned[i+1]):
                ans += 1
        return ans
