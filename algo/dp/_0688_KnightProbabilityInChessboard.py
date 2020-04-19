class Solution:
    
    # DFS with Memoization (DP) [60%]
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        pathSuccess = self.dfs(N, K, r, c, {}) 
        pathTotal   = 8 ** K
        #print(pathSuccess, pathTotal)
        return pathSuccess / pathTotal
        
    def dfs(self, N, k, r, c, memo):
        if r < 0 or r >= N or c < 0 or c >= N:
            return 0 
        if k == 0:
            return 1
        if (k, r, c) in memo:
            return memo[(k, r, c)]
        
        dirs = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        ans = 0 
        for d in dirs:
            ans += self.dfs(N, k-1, r - d[0], c - d[1], memo)
        memo[(k, r, c)] = ans
        return ans 
        
    # BFS, correct but too slow  [TLE] 
    def knightProbability1(self, N: int, K: int, r: int, c: int) -> float:
        
        dirs = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        queue = collections.deque([(r,c)])
        
        failCount = 0 
        pathCount = 0 
        
        while K > 0:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for d in dirs:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]
                    if x < 0 or x >= N or y < 0 or y >= N:
                        failCount += 8 ** (K - 1) #probability calculation needs to go to the final leaves
                        pathCount += 8 ** (K - 1) #probability calculation needs to go to the final leaves
                        continue
                    if K == 1:
                        pathCount += 1
                    queue.append((x, y))
            K -= 1
            #print("fail:", failCount, "total:", pathCount)
        return 1 - (failCount / pathCount)