class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDis= max(arr)-min(arr)
        l=[]
        arr.sort()
        for i in range(1,len(arr)):
            minDis= min(minDis,arr[i]-arr[i-1])
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==minDis:
                l.append([arr[i-1],arr[i]])
        return l
