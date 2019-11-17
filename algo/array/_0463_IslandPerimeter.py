class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0: 
            return 0
        
        m = len(grid)
        n = len(grid[0])
        neighbors = [[0 for j in range(n)] for i in range(m)]
        perimeter = 0
        for i in range(m):
            for j in range(n):
                self.updateSurroundings(grid, i, j, neighbors)
                if grid[i][j] == 1:
                    perimeter += 4 - neighbors[i][j]
        # print(grid)
        # print(neighbors)
        return perimeter
    
    def updateSurroundings(self, grid, i, j, neighbors):
        # print(i, j)
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        ni, nj = i-1, j
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
            count += 1
        
        ni, nj = i+1, j
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
            count += 1
        
        ni, nj = i, j-1
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
            count += 1
        
        ni, nj = i, j+1
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
            count += 1
            
        neighbors[i][j] = count
    