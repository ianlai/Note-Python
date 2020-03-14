class Solution:
    #===================================
    # Best: 40%
    # use different array in each level) 
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []
        ans = []
        self.dfs(n, k, ans, [], 1)
        return ans
    
    def dfs(self, n, k, ans, cur, nidx):
        if len(cur) == k:
            ans.append(cur)
            return 
        for i in range(nidx, n + 1):
            self.dfs(n, k, ans, cur + [i], i + 1)
        return 
    
    #===================================
    # OK: 20%
    # use cur one array to do the traverse, 
    # only clone to new in the end 
    def combine2(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []
        ans = []
        self.dfs2(n, k, ans, [], 1)
        return ans
    
    def dfs2(self, n, k, ans, cur, nidx):
        if len(cur) == k:
            #ans.append(list(cur))   #create new array (ok)
            #ans.append(cur[:])      #create new array (ok)
            ans.append(cur + [])     #create new array (ok)
            return 
        for i in range(nidx, n + 1):
            cur.append(i)
            self.dfs2(n, k, ans, cur, i + 1)
            cur.remove(i)
        return 
    
    #===================================
    ## Fine, but not preferred, actually kidx not necessary 
#     def combine2(self, n: int, k: int) -> List[List[int]]:
#         if n == 0 or k == 0:
#             return []
#         ans = []
#         self.bfs2(n, k, ans, [], 1, 0)
#         return ans
    
#     def bfs2(self, n, k, ans, cur, nidx, kidx):
#         if kidx == k:
#             ans.append(cur)
#             return 
#         for i in range(nidx, n + 1):
#             self.bfs2(n, k, ans, cur + [i], i + 1, kidx + 1)
#         return 