class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        row,col=len(matrix),len(matrix[0])
        height =[0]*col
        max_area=0

        for r in range(row):
            for c in range(col):
                if matrix[r][c]=='1':
                    height[c] += 1
                else:
                    height[c]=0

            stack=[]
            for i in range(col+1):
                curHeight = height[i] if i < col else 0

                while stack and curHeight < height[stack[-1]]:
                    h= height[stack.pop()]
                    width =i if not stack else i-stack[-1]-1
                    max_area=max(max_area,h*width)
                stack.append(i)
        return max_area
        
