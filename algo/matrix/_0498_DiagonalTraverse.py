class Solution:
    
    # Index i + j should be in the same group [O(MN), 68% - 97%]
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        M, N = len(matrix), len(matrix[0])
        arrays = [ [] for _ in range((M + N - 1))] 
        ans = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                idx = i + j
                arrays[idx].append(matrix[i][j])
        
        for i in range(len(arrays)):
            if i % 2 == 0:
                arrays[i] = arrays[i][::-1]
            ans.extend(arrays[i])
        
        return ans