class Solution:
    
    #BFS: Better use BFS since we should avoid using recursion which we will use for DFS (16%)
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        count = 0 
        m, n = len(grid), len(grid[0])
        visited = set() #record the visited points of the island (value is 1)
        
        # Traverse 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    self.bfs(grid, (i,j), visited)
        return count 
    
    def bfs(self, grid, start, visited):
        q = collections.deque([start])
        visited.add(start)
        #print("start:", start)
        while q:
            point = q.popleft()
            #print(" point:", point)
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                newi = point[0] + di
                newj = point[1] + dj 
                if not self.isValid(grid, newi, newj) or (newi, newj) in visited:
                    continue
                q.append((newi, newj))
                visited.add((newi, newj))
                
    def isValid(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m:
            return False
        if j < 0 or j >= n:
            return False
        return grid[i][j] == "1"
    
    #======================================        
        
        
    #DFS (71%)
    def numIslands1(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 :
            return 0
        count = 0
        print("row:", len(grid), " col:", len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(grid[i][j], end="")
                if grid[i][j] == "1":
                    count += 1
                    self.foundIsland(grid, i,j)
            #print()
        return count
                    
    def foundIsland(self, grid, i, j):
        if i < 0 or i >= len(grid):
            return 
        if j < 0 or j >= len(grid[0]):
            return 
        if grid[i][j] == "0":
            return 
        elif grid[i][j] == "1":
            grid[i][j] = "0"
            self.foundIsland(grid, i-1, j)
            self.foundIsland(grid, i+1, j)
            self.foundIsland(grid, i, j-1)
            self.foundIsland(grid, i, j+1)
        