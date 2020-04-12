class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        
        #1. Define state = steps from start 
        
        #2. Initialize
        f = [[0 for j in range(n)] for i in range(m)]  
        for i in range(m):
            f[i][0] = 1
        for j in range(n):
            f[0][j] = 1
        
        #3. Transition 
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        
        #4. Answer
        return f[m-1][n-1]
        