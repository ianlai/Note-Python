class Solution:
    # Method-1
    # Get the unit perimeter when scaning to that cell; update overall perimeter immediately 
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0: 
            return 0
        
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += self.calUnitPerimeter(grid, i, j)
        return perimeter
    
    def calUnitPerimeter(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        vectors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for v in vectors:
            ni, nj = v[0], v[1]
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                count += 1

        return 4 - count
    
    # Method-2
    # Use a neighbor matrix to record the number of neighbors (not necessary, show)
    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0: 
            return 0
        
        m = len(grid)
        n = len(grid[0])
        neighbors = [[0 for j in range(n)] for i in range(m)]
        perimeter = 0
        for i in range(m):
            for j in range(n):
                self.updateSurroundings1(grid, i, j, neighbors)
                if grid[i][j] == 1:
                    perimeter += 4 - neighbors[i][j]
        # print(grid)
        # print(neighbors)
        return perimeter
    
    def updateSurroundings1(self, grid, i, j, neighbors):
        # print(i, j)
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        vectors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for v in vectors:
            ni, nj = v[0], v[1]
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                count += 1

        neighbors[i][j] = count