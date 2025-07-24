class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        l = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  #skip duplicate i
            left, right = i + 1, len(nums) - 1
            while left < right:  #protect from going out of loop
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    l.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  #skip duplicate left
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  #skip duplicate right
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return l
