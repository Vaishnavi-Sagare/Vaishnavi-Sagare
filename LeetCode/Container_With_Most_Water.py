class Solution(object):
    def maxArea(self, height):
        water=0
        l=0
        r=len(height)-1
        while l<r:
            x=(r-l)*min(height[l],height[r])
            water=max(x,water)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return water
