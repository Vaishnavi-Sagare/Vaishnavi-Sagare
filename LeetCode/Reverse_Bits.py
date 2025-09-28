class Solution:
    def reverseBits(self, n: int) -> int:
        n1=bin(n)[2:].zfill(32)
        n1=n1[::-1]
        return int(n1,2)
