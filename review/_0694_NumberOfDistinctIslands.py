class Solution:
    
    # DFS (ref) [O(n), 55%]
    def numDistinctIslands(self, grid):
        seen = set()
        def explore(r, c, r0, c0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add((r - r0, c - c0))
                explore(r+1, c, r0, c0)
                explore(r-1, c, r0, c0)
                explore(r, c+1, r0, c0)
                explore(r, c-1, r0, c0)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c, r, c)
                if shape:
                    shapes.add(frozenset(shape))
        return len(shapes)
    
    #=================================================
    
    # 2020.08.08 
    # BFS [O(n), 59%]
    # Enhanced: remove visited array (set it to 0 instead)
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        print("BFS-2")
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0
        
        #visited = set([])
        islands = set([])
        numOfIsland = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numOfIsland += self.bfs(grid, i, j, [], islands)
        return numOfIsland
        
    def bfs(self, grid, i, j, curIsland, islands):
        if not self.isValid(grid, i, j):
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        deque = collections.deque([(i,j)])
        
        while deque:
            cur = deque.popleft()
            for d in directions:
                nxt = (cur[0] + d[0], cur[1] + d[1])
                if not self.isValid(grid, nxt[0], nxt[1]):
                    continue
                deque.append(nxt)
                grid[nxt[0]][nxt[1]] = 0 #same as "setting visited"
                curIsland.append(nxt)
                
        island = []
        for cur in curIsland:
            #cur = visited.pop()  #can't pop out the visited
            normalizedI = cur[0] - i
            normalizedJ = cur[1] - j
            island.append((normalizedI, normalizedJ))
        islandTuple = tuple(island)      #to become hashable (for in operator)
        
        if islandTuple not in islands:
            islands.add(islandTuple)        
            return 1
        else:
            return 0 
                
    def isValid(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if not(0 <= i < m): return False
        if not(0 <= j < n): return False
        if grid[i][j] == 0: return False
        return True

    #=================================================
    
    # 2020.05.01
    # BFS [O(n), 29%]
    def numDistinctIslands1(self, grid: List[List[int]]) -> int:
        print("BFS-1")
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
                numOfIsland += self.bfs1(grid, i, j, visited, [], islands)
        return numOfIsland
        
    def bfs1(self, grid, i, j, visited, curIsland, islands):
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
                if not self.isValid1(grid, nxt[0], nxt[1], visited):
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
                
                
    def isValid1(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        if not(0 <= i < m): return False
        if not(0 <= j < n): return False
        if grid[i][j] == 0: return False
        if (i, j) in visited: return False
        return True