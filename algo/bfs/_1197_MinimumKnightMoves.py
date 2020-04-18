class Solution:
    
    # DFS with memoization; pruning to first quadrant [79%]
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        return self.helper(abs(x), abs(y), {})
    
    def helper(self, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        if (x, y) == (0, 0):
            return 0 
        if (x, y) == (1, 0) or (x,y) == (0, 1):
            return 3 
        if (x, y) == (1, 1):
            return 2
        
        # Only consider first quadreant 
        # The best solution should always come from left or lower (2 options) even though there are total 8 options (pruning)
        ans = min(self.helper(abs(x-2), abs(y-1), memo), self.helper(abs(x-1), abs(y-2), memo)) + 1 
        memo[(x, y)] = ans
        return ans

    #====================================================
    
    # BFS with pruning to first quadrant and x > y [54%]
    def minKnightMoves1(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        
        #Use symmetry to prune the paths
        x, y = abs(x), abs(y)
        if y > x:
            x, y = y, x
        
        dirs = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]
        visited = set([])
        queue = collections.deque([(0,0)])
        count = 0 
        while queue:
            for cur in range(len(queue)):
                cur = queue.popleft()
                
                #If we set continue when x or y smaller than 0, 
                #some test cases close to x-axis or y-axis will be incorrect, e.g. (1,1)
                if cur[0] < -2 or cur[1] < -2: 
                    continue
                if cur[0] < cur[1]:
                    continue
                if cur == (x, y):
                    return count
                if cur in visited:
                    continue
                else: 
                    visited.add(cur)
                for d in dirs:
                    queue.append((cur[0] + d[0], cur[1] + d[1]))
            count += 1
    
    #====================================================
    
    # BFS with pruning to first quadrant [39%]
    def minKnightMoves2(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        
        #Use symmetry to prune the paths
        x, y = abs(x), abs(y)
        
        dirs = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]
        visited = set([])
        queue = collections.deque([(0,0)])
        count = 0 
        while queue:
            for cur in range(len(queue)):
                cur = queue.popleft()
                
                #If we set continue when x or y smaller than 0, 
                #some test cases close to x-axis or y-axis will be incorrect, e.g. (1,1)
                if cur[0] < -2 or cur[1] < -2: 
                    continue
                if cur == (x, y):
                    return count
                if cur in visited:
                    continue
                else: 
                    visited.add(cur)
                for d in dirs:
                    queue.append((cur[0] + d[0], cur[1] + d[1]))
            count += 1