class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if m == 0 or n == 0:
            return []
        
        parent = {}
        lands = set([])
        ans = []
        self.count = 0
        self.n = n
            
        for i, p in enumerate(positions):
            curIdx = self.xyToIdx(p)
            
            #point existed
            if curIdx in lands:
                ans.append(ans[-1])
                continue
            
            # new point
            parent[curIdx] = -1 
            self.count += 1
            lands.add(curIdx)
            
            for dp in [(1,0), (-1,0), (0,1), (0,-1)]:
                newp = [p[0] + dp[0], p[1] + dp[1]]
                if not (0 <= newp[0] < m and 0 <= newp[1] < n):
                    continue
                newIdx = self.xyToIdx(newp)
                if newIdx in lands:
                    tempCount = self.count
                    self.union(parent, curIdx, newIdx)
                        
            ans.append(self.count)
        
        return ans
                            
    def xyToIdx(self, p):
        return p[0] * self.n + p[1]
    
    def union(self, parent, a, b):
        rootA = self.find(parent, a)
        rootB = self.find(parent, b)
        
        if rootA != rootB:
            parent[rootA] = rootB
            #print("union!!", a, b)
            self.count -= 1    
        
    def find(self, parent, a):
        if parent[a] == -1:
            return a
        else:
            return self.find(parent, parent[a])