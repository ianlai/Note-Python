class Solution:
    
    # Memoization DP
    def minPathSum(self, grid: List[List[int]]) -> int:
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
        
        
        