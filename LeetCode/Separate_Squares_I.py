class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area=0.0
        for i in range(len(squares)):
            total_area += (squares[i][2]*squares[i][2])
        half = total_area/2.0

        def lower_area(k):
            area=0.0
            for x,y,l in squares:
                if k <= y:
                    continue
                elif k>= (y+l):
                    area += (l*l)
                else:
                    area += (k-y)*l
            return area
        
        low = min(y for x,y,l in squares)
        high = max(y+l for x,y,l in squares)
        for i in range(60):
            mid = (low + high) / 2
            if lower_area(mid)<half:
                low = mid
            else :
                high = mid
        return low
