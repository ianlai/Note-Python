class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if A is None or len(A) < 2: 
            return -1
        
        A.sort()
        start, end = 0, len(A) -1 
        S = -sys.maxsize 
        exist = False
        
        while start < end: 
            sum = A[start] + A[end]
            if sum >= K:
                end -= 1
            else:
                S = max(S, sum)
                exist = True
                start += 1
                
        if exist == True:
            return S
        else:
            return -1
                
        