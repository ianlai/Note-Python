class Solution:
    
    #DFS (Traverse twice) [12%]
    def numEnclaves(self, A: List[List[int]]) -> int:
        if len(A) == 0:
            return 0
        m, n = len(A), len(A[0])
        
        # Traverse 1: Find the land connected to the boarders and make them to water
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    self.dfs(A, i, j, 0, None)
        
        # Traverse 2: Find the land not connected to the boarders, make them to water, count up by the number of lands
        counter = [0]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, i, j, 0, counter)
                    
        return counter[0]
    
    def dfs(self, A, i, j, val, counter):
        m, n = len(A), len(A[0])
        if not (0 <= i < m and 0 <= j < n):
            return
        
        if A[i][j] == 0:
            return 
        
        A[i][j] = 0 
        if counter:
            counter[0] += 1
        
        self.dfs(A, i + 1, j, 0, counter)  
        self.dfs(A, i - 1, j, 0, counter)  
        self.dfs(A, i, j + 1, 0, counter)  
        self.dfs(A, i, j - 1, 0, counter)  