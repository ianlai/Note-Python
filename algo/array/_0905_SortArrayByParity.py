class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if A is None or len(A) == 0:
            return []
        
        ans = [0] * len(A)
        even, odd = 0, len(A) - 1
        for i in range(len(A)):
            if A[i] % 2 == 0:  #even
                ans[even] = A[i]
                even += 1
            else:
                ans[odd] = A[i]
                odd -= 1
        
        return ans
        