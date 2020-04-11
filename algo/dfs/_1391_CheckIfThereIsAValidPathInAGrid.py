class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if len(grid) == 0:
            return False
        
        # Map of direction to the possible street blocks  
        self.dirToS = {   
            'r': [1,3,5],
            'u': [2,3,4],
            'l': [1,4,6],
            'd': [2,5,6]
        }
        # Map of street block to the directions it leads to 
        self.sToDir = {
            1 : ['r', 'l'],
            2 : ['u', 'd'],
            3 : ['l', 'd'],
            4 : ['r', 'd'],
            5 : ['l', 'u'],
            6 : ['r', 'u']  
        }
        # Map of direction to the coordinate shifts
        self.dirToXy = {
            'r': ( 0,  1),
            'u': (-1,  0),
            'l': ( 0, -1),
            'd': ( 1,  0)
        }
        
        visited = set([])   #must use set (TLE if using list)
        return self.helper(grid, 0, 0, visited)
    
    def helper(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        
        if (i, j) == (m-1, n-1): #arrived at the destination 
            return True
        
        cur = grid[i][j]
        nextDirs = self.sToDir[cur] 
		
        for nextDir in nextDirs:  #nextDir: 'r', 'u', 'l', 'd'
            ni = i + self.dirToXy[nextDir][0] #next i
            nj = j + self.dirToXy[nextDir][1] #next j 
            
            if ni < 0 or ni >= m or nj < 0 or nj >= n: #out of the boundary 
                continue
            if grid[ni][nj] not in self.dirToS[nextDir]: #street blocks not matching 
                continue
            if (ni, nj) in visited: #visited 
                continue
                
            visited.add((ni, nj))
            if self.helper(grid, ni, nj, visited): 
                return True
            visited.remove((ni, nj)) #backtracking 
            
        return False