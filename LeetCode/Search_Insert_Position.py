class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        for i in nums:
            mid=(low+high)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        for i in range(len(nums)-1):
            if target>=nums[i] and target<=nums[i+1]:
                return i+1
            elif target < nums[0]:
                return 0
            elif target> nums[-1]:
                return len(nums)
            else:
                pass
