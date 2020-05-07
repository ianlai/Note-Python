from collections import defaultdict
class Solution:
    
    # Union Find [12%]
    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            print(i, grid[i])
            
        parent = defaultdict()
        self.count = 0
        
        # Create number of nodes with num of "1" 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    parent[i * n + j] = -1
                    print("node:", i*n+j, "->", parent[i * n + j])
                    self.count += 1
                    
        # Traverse them to union the adjacent nodes 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                        newi, newj = i + di, j + dj
                        if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == "1":
                            self.union(parent, i * n + j, newi * n + newj)
        return self.count 

    def find(self, parent, i):
        if parent[i] != -1:
            return self.find(parent, parent[i])
        else:
            return -1

    def union(self, parent, a, b):
        rootA = self.find(parent,a)
        rootB = self.find(parent,b)
        
        if rootA != rootB:            
            ### Naive union 
            parent[rootA] = rootB
            self.count -= 1
            
    
    #========================================================  

    # Union Find [O(n2 * average tree depth) 12%]
    def numIslands2(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            print(i, grid[i])
            
        parent = defaultdict()
        self.count = 0
        
        # Create number of nodes with num of "1" 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    parent[i * n + j] = -1
                    print("node:", i*n+j, "->", parent[i * n + j])
                    self.count += 1
                    
        # Traverse them to union the adjacent nodes 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                        newi, newj = i + di, j + dj
                        if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == "1":
                            self.union(parent, i * n + j, newi * n + newj)
        return self.count 

    def find(self, parent, i):
        if parent[i] != -1:
            return self.find(parent, parent[i])
        else:
            return i

    def union(self, parent, a, b):
        rootA = self.find(parent,a)
        rootB = self.find(parent,b)
        
        if rootA != rootB:            
            ### Naive union 
            parent[rootA] = rootB
            self.count -= 1
            
    #========================================================  
    
    # BFS, set point to 0 once traversed  [24%]
    def numIslands3(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        count = 0 
        m, n = len(grid), len(grid[0])
        ### visited = set() #record the visited points of the island (value is 1)
        
        # Traverse 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(grid, (i,j))
        return count 
    
    def bfs(self, grid, start):
        q = collections.deque([start])
        while q:
            point = q.popleft()
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                newi = point[0] + di
                newj = point[1] + dj 
                if not self.isValid(grid, newi, newj):
                    continue
                q.append((newi, newj))
                grid[newi][newj] = 0 
                
    def isValid(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m:
            return False
        if j < 0 or j >= n:
            return False
        return grid[i][j] == "1"
    
    #========================================================     
    
    # BFS, add point to set once traversed [24%]
    # (Better use BFS since we should avoid using recursion which we will use for DFS)
    def numIslands1(self, grid: List[List[str]]) -> int:
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
                    self.bfs1(grid, (i,j), visited)
        return count 
    
    def bfs1(self, grid, start, visited):
        q = collections.deque([start])
        visited.add(start)
        #print("start:", start)
        while q:
            point = q.popleft()
            #print(" point:", point)
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                newi = point[0] + di
                newj = point[1] + dj 
                if not self.isValid1(grid, newi, newj) or (newi, newj) in visited:
                    continue
                q.append((newi, newj))
                visited.add((newi, newj))
                
    def isValid1(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m:
            return False
        if j < 0 or j >= n:
            return False
        return grid[i][j] == "1"
    
    #========================================================      
        
    #DFS, set point to 0 once traversed [71%]
    def numIslands2(self, grid: List[List[str]]) -> int:
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
        