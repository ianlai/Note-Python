class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if A is None or len(A)==0:
            return []
        
        ans = []
        for i in range(len(A[0])): #must be len(A[0]), not len(A)
            ans.append([])

        for i in range(len(A)):
            for j in range(len(A[i])):
                ans[j].append(A[i][j])
        
        return ans
                    
                