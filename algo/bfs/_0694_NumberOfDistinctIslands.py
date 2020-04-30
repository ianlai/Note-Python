class Solution:
    
    # BFS [ 8% ]
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0
        
        #for i in range(m):
        #    print(grid[i])
        
        visited = set([])
        islands = set([])
        numOfIsland = 0
        
        for i in range(m):
            for j in range(n):
                numOfIsland += self.bfs(grid, i, j, visited, [], islands)
        return numOfIsland
        
    def bfs(self, grid, i, j, visited, curIsland, islands):
        if not self.isValid(grid, i, j, visited):
            return 0
        
        #print("BFS:", i, j, visited)
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        deque = collections.deque([(i,j)])
        
        while deque:
            cur = deque.popleft()
            for d in directions:
                nxt = (cur[0] + d[0], cur[1] + d[1])
                if not self.isValid(grid, nxt[0], nxt[1], visited):
                    continue
                #print("  nxt:", nxt)
                deque.append(nxt)
                visited.add(nxt)
                curIsland.append(nxt)
                
        #print("visited:", visited)
        island = []
        for cur in curIsland:
            #cur = visited.pop()  #can't pop out the visited
            normalizedI = cur[0] - i
            normalizedJ = cur[1] - j
            island.append((normalizedI, normalizedJ))
        islandTuple = tuple(island) #to become hashable (for in operator)
        
        #print("island(list):", island)
        #print("island(tuple):", islandTuple)
        if islandTuple not in islands:
            islands.add(islandTuple)        
            return 1
        else:
            #print("island existed:", islandTuple)
            return 0 
                
                
    def isValid(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        if not(0 <= i < m): return False
        if not(0 <= j < n): return False
        if grid[i][j] == 0: return False
        if (i, j) in visited: return False
        return True
            
            
        