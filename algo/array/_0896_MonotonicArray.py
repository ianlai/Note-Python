class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A is None or len(A) == 0:
            return True
        
        isIncreasing = None
        for i in range(len(A)):
            if i > 0 and i < len(A):
                if   A[i-1] < A[i]:
                    if isIncreasing == False:
                        return False
                    isIncreasing = True
                elif A[i-1] > A[i]:
                    if isIncreasing == True:
                        return False
                    isIncreasing = False
                #elif A[i-1] == A[i]: 
   
        return True