class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i,ans=0,0
        while ans<=n:
            if n== (2**i):
                return True
            ans= (2**i)
            i += 1
        return False
