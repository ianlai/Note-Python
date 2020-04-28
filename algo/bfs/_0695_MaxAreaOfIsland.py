class Solution:
    
    #BFS [24%]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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
                
    # DFS, wrong!!
#     def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
#         if len(grid) == 0 or len(grid[0]) == 0:
#             return 0
        
#         visited = set()
#         ans = [0, 0]  #max area, cur area
        
#         for i in range(len(grid)):
#             print(grid[i])
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 self.helper(grid, (i, j), visited, ans)
                
#         return ans[0]
                
    
#     def helper(self, grid, cur, visited, ans):
#         if cur[0] == len(grid) or cur[1] == len(grid[0]):
#             return 
#         if cur in visited:
#             return 
#         if grid[cur[0]][cur[1]] == 0:
#             ans[1] = 0
#             return 
        
#         visited.add(cur)
    
#         ans[1] += 1 
#         ans[0] = max(ans[0], ans[1])
#         print(cur, ans)
            
#         directions = [(1,0), (-1,0), (0,1), (0,-1)]
#         for d in directions:
#             nxt = (cur[0] + d[0], cur[1] + d[1])
#             visited.add(nxt)
#             self.helper(grid, nxt, visited, ans)
        