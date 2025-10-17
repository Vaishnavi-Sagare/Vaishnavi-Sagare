class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        f=Counter(nums)
        sum=0
        for key,v in f.items():
            if v%k==0:
                sum += key*v
        return sum
