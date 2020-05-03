class Solution:
    
    # With template (OOXX) //not return in loop 
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:
            return -1
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[mid+1]:  #right part
                end = mid
            else:        
                start = mid   
        if A[start] > A[end]:
            return start 
        return end
    
    # Without template  //return in loop
    def peakIndexInMountainArray1(self, A: List[int]) -> int:
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