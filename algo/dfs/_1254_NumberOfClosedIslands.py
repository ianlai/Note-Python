class Solution:

    # DFS (traverse twice) [21%]
    def closedIsland(self, grid):
        print("Traverse twice")
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, val):  #make all become val 
            if 0 <= i < m and 0 <= j < n and grid[i][j]==0:
                grid[i][j] = val  
                dfs(i, j+1, val)
                dfs(i+1, j, val)
                dfs(i-1, j, val)
                dfs(i, j-1, val)
        
        # Traverse1: make the land on the boarder to the water (1)
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j, 1)
        
        # Traverse2: make the inside land to the water, and count 1 up 
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1
                    
        return res
    
    #=======================================================
    
    # DFS (mark out of boarder in a traversal) [14%]
    # Use a variable to record whether there is any out of board during this traversal 
    def closedIsland1(self, grid: List[List[int]]) -> int:
        print("Record out of board")
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
