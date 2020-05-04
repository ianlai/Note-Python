class Solution:
    
    #BFS: [57%, O(mn)]
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze:
            return False
        if start == destination:
            return True
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        deque = collections.deque([start])
        visited = set([])
        
        while deque:
            cur = deque.popleft()
            if tuple(cur) in visited:
                continue
            visited.add(tuple(cur))
            #print("cur:", cur)
            for d in directions:
                end = self.goToEnd(maze, cur, d)
                #print(">>", "d:", d, "end:", end)
                if end == destination:
                    return True
                deque.append(end) 
            #print("deque:", deque)
            #print("visited:", visited)
            #print("------------")
        return False
                
    def goToEnd(self, maze, cur, d):
        cur0, cur1 = cur[0], cur[1]
        while True:
            next0, next1 = cur0 + d[0], cur1 + d[1]
            if not (0 <= next0 < len(maze) and 0 <= next1 < len(maze[0])):
                return [cur0, cur1]
            if maze[next0][next1] == 1:
                return [cur0, cur1]
            cur0, cur1 = next0, next1
            
            