class Solution:
    
    #2020.08.08
    #DFS [O(n), 92%]
    #Simply set the traversed land to water to avoid traversing twice
    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        print("DFS-2")
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        maxArea = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0 #traversed, so set it to be water
            area = 1       #count this one
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            return area
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
    
    #======================================================
    #2020.04.30 
    #BFS [24%]
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        print("BFS")
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        if len(grid) == 1 and len(grid[0]) == 1:
            if grid[0][0] == 0:
                return 0
            else:
                return 1
        
        deque = collections.deque([])
        visited = set()
        ans = [0, 0]  #max area, cur area
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in range(len(grid)):
            print(grid[i])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                visited.add((i,j))
                if grid[i][j] == 1:
                    ans[1] = 1
                    ans[0] = max(ans[0], ans[1])
                    deque.append((i,j))
                    while deque:
                        cur = deque.popleft()
                        #print(cur, ans)
                        for d in directions:
                            nxt = (cur[0] + d[0], cur[1] + d[1])
                            if (nxt[0] < 0 or nxt[0] == len(grid) or
                                nxt[1] < 0 or nxt[1] == len(grid[0]) or
                                grid[nxt[0]][nxt[1]] == 0 or
                                nxt in visited): 
                                continue
                            ans[1] += 1
                            ans[0] = max(ans[0], ans[1])
                            #print(" ", ans)
                            deque.append(nxt)
                            visited.add(nxt)
                    ans[1] = 0
        return ans[0]
    
    #======================================================
    
    #DFS [O(n), 33%]
    #Use a set to store the visited to avoid traversing twice
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        print("DFS")
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        visited = set()
        
        #max area (calculated by return value)
        #max area (calculated by array value)  <-- incorrect
        #cur area (array value)                <-- incorrect
        ans = [0, 0, 0]  
        
        for i in range(len(grid)):
            print(grid[i])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print("traverse: ", i, j)
                self.helper(grid, (i, j), visited, ans)
        return ans[0]
    
    def helper(self, grid, cur, visited, ans):
        if cur in visited:
            return 0
        if cur[0] < 0 or cur[0] >= len(grid) or cur[1] <0 or cur[1] >= len(grid[0]):
            return 0
        
        if grid[cur[0]][cur[1]] == 0:
            ans[1] = 0
            return 0
        
        visited.add(cur)
        area = 1 #cur area (return value)
            
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for d in directions:
            nxt = (cur[0] + d[0], cur[1] + d[1])
            area += self.helper(grid, nxt, visited, ans)
            visited.add(nxt)
            
        ans[2] += 1 #not correct, all the islands' land will be added together
                    #we need to judge the connectivity either (1) one-layer out of the recursion or (2) by adding extra conditions here
                    #(2) adding extra conditions are duplicated code 
                    #(1) judging outside is easier, but then we should use return value instead of array stored value
                    #besides, using array to store means we only have one position to store the data, which might be a weak point
                    
        ans[0] = max(ans[0], area)
        ans[1] = max(ans[1], ans[2])
        #print("cur:", cur)
        #print("maxArea(return):", ans[0], "maxArea(array):", ans[1])
        #print("curArea(return):", area,   "curArea(array):", ans[2])
        
        return area 
    
    #======================================================
    
    #(Ref) DFS [28%]
    def maxAreaOfIsland0(self, grid):
        print("DFS (ref)")
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            
            curArea = 1 + \
                    area(r+1, c) + \
                    area(r-1, c) + \
                    area(r, c-1) + \
                    area(r, c+1)
            return curArea

        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxArea = max(area(r, c), maxArea)
                #print(r, c, seen)
        return maxArea