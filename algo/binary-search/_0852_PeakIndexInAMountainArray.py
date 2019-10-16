class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if A is None or len(A) == 0:
            return -1
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] < A[mid+1]: #go right
                start = mid 
            elif A[mid-1] > A[mid] > A[mid+1]: #go left
                end = mid 
            else:        
                start = mid                    #go either (right), TLE if missing this      
        return -1