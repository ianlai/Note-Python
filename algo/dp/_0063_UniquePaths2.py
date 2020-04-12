class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        
        #1. Define state = steps from start 
        
        #2. Initialize
        f = [[0 for j in range(n)] for i in range(m)]  
        f[0][0] = 1
        
        #3. Transition 
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        f[i][j] = f[i][j-1]
                    elif j == 0:
                        f[i][j] = f[i-1][j] 
                    else:
                        f[i][j] = f[i-1][j] + f[i][j-1]
                        
        #4. Answer
        return f[m-1][n-1]
        