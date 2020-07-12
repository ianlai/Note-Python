class Solution:
    
    # DFS [14%]
    # Use a global variable to record whether there is any out of board during this traversal 
    def closedIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        isOutside = [False]
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):    
                if grid[i][j] == 0:
                    self.dfs(grid, i, j, isOutside)
                    if isOutside[0] == False:
                        counter += 1
                isOutside = [False]
        return counter
                    
    def dfs(self, grid, i, j, isOutside):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            isOutside[0] = True
            return 
        if grid[i][j] == 1:
            return 
        grid[i][j] = 1  #visited 
        
        self.dfs(grid, i+1, j, isOutside)
        self.dfs(grid, i-1, j, isOutside)
        self.dfs(grid, i, j+1, isOutside)
        self.dfs(grid, i, j-1, isOutside)
