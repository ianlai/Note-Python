class Solution:
    
    # BFS [75%]
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) == 0 or len(M[0]) == 0:
            return 0
        m = len(M)
        self.debug(M)
        deque = collections.deque([])
        visited = set([])
        count = 0
        
        for i in range(m):
            if i in visited:
                continue
            deque.append(i)
            while deque:
                cur = deque.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                for j in range(m):
                    if cur != j and M[cur][j] == 1:
                        deque.append(j)
            count += 1
        return count 
                
    # ========================================== 
    # DFS [75%]
    def findCircleNum1(self, M: List[List[int]]) -> int:
        if len(M) == 0 or len(M[0]) == 0:
            return 0
        m = len(M)
        
        #self.debug(M)
        
        count = 0
        visited = set([])
        for i in range(m):
            if i not in visited and self.dfs(M, i, visited) == 1:
                count += 1 
                #print("count:", count, "idx:", i, visited)
            visited.add(i)
        return count
        
    def dfs(self, M, cur, visited):
        if cur in visited:
            return 0
        visited.add(cur)
        for i in range(len(M)):
            #if i > cur and M[cur][i] == 1:  #WRONG! 
            if M[cur][i] == 1:
                self.dfs(M, i, visited)
        return 1
    
    # ==========================================        
    # Union Find [9%]
    def findCircleNum1(self, M: List[List[int]]) -> int:
        if len(M) == 0 or len(M[0]) == 0:
            return 0
        m = len(M)
        
        #self.debug(M)
            
        # Initialize
        parent = {}
        self.count = 0
        for i in range(m):
            parent[i] = -1
            self.count += 1    
        #print("count: ", self.count)
            
        # Traverse and union
        for i in range(m):
            for j in range(m):
                if i < j and M[i][j] == 1:
                    self.union(parent, i, j)
                    
        return self.count 
    
    def union(self, parent, a, b):
        #print("union:", a, b)
        rootA = self.find(parent, a)
        rootB = self.find(parent, b)
        if rootA != rootB:
            parent[rootA] = rootB
            self.count -= 1
        
    def find(self, parent, a):
        if parent[a] == -1:
            return a
        else:
            return self.find(parent, parent[a])
    
    # Debug
    def debug(self, M):
        for i in range(len(M)):
            print(i, M[i])
                
        