class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result=[]
        start_col=s[0]
        end_col=s[3]
        start_row=int(s[1])   
        end_row=int(s[4])
        for i in range(ord(start_col),ord(end_col)+1):
            for j in range(start_row, end_row + 1):
                result.append(chr(i)+str(j))
        return result  
