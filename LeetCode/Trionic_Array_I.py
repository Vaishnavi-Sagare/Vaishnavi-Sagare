class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        if len(nums) < 3 or nums[1] <= nums[0]:
            return False
        inc1, dec, inc2 = 0, 1, 2
        state = inc1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return False

            if state == inc1:
                if nums[i]>nums[i-1]:
                    continue
                else:
                    state = dec
            elif state == dec:
                if nums[i]<nums[i-1]:
                    continue
                else:
                    state = inc2
            else:
                if nums[i]>nums[i-1]:
                    continue
                else:
                    return False

        return state==inc2
