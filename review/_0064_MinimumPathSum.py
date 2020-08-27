class Solution:
    
    # Bottom-up DP [81%]
    def minPathSum(self, grid: List[List[int]]) -> int:
        print("Buttom-Up DP")
        if len(grid) == 0:
            return 0 
        m, n = len(grid), len(grid[0])
        dp = [[grid[i][j] for j in range(n)] for i in range(m)]  #clone grid matrix
        
        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
            
        for i in range(1, n):
            dp[0][i] += dp[0][i-1]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                
        return dp[m-1][n-1]
          
        # debug:
        # for i in range(m):  
        #     print(i, dp[i])
    
    # ================================================
    
    # Top-down DP [25%]
    def minPathSum1(self, grid: List[List[int]]) -> int:
        print("Top-Down DP")
        if len(grid) == 0:
            return 0
        memo = {}
        ans = self.dp(grid, 0, 0, memo)
        print(memo)
        return ans
        
    def dp(self, grid, x, y, memo):  #(x,y) definition is not the definitation of math
        m, n = len(grid), len(grid[0])
        if x == m or y == n:
            return 0
        if (x, y) in memo:
            return memo[(x,y)]
        right = self.dp(grid, x, y + 1, memo)
        down  = self.dp(grid, x + 1, y, memo)
        
        memo[(x,y)] = grid[x][y]

        if x == m - 1:
            memo[(x,y)] += right
        elif y == n - 1:
            memo[(x,y)] += down
        else:
            memo[(x,y)] += min(right, down)
        
        return memo[(x,y)] 
        
        
        