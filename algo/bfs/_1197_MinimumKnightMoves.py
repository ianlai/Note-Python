class Solution:
    
    # BFS with pruning [39%]
    def minKnightMoves(self, x: int, y: int) -> int:
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
                
        