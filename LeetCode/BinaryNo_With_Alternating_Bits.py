class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ans=str(bin(n))
        for i in range(2,len(ans)-1):
            if ans[i]==ans[i+1]:
                return False
        return True
