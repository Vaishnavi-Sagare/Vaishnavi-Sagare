class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum=0
        for i in range(len(columnTitle)):
            res= ord(columnTitle[i])-64
            sum = sum*26 + res
        return sum
