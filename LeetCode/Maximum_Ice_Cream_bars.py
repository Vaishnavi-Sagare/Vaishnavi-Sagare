class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n,i=0,0
        while i<len(costs) and coins>=costs[i]:
            n +=1
            coins -= costs[i]
            i += 1
        return n
