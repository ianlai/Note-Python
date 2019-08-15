class Solution:
    
    ### OK
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []
        ans = []
        self.bfs(n, k, ans, [], 1)
        return ans
    
    def bfs(self, n, k, ans, cur, nidx):
        if len(cur) == k:
            ans.append(cur)
            return 
        for i in range(nidx, n + 1):
            self.bfs(n, k, ans, cur + [i], i + 1)
        return 
    
      ### OK, but kidx not necessary 
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         if n == 0 or k == 0:
#             return []
#         ans = []
#         self.bfs(n, k, ans, [], 1, 0)
#         return ans
    
#     def bfs(self, n, k, ans, cur, nidx, kidx):
#         if kidx == k:
#             ans.append(cur)
#             return 
#         for i in range(nidx, n + 1):
#             self.bfs(n, k, ans, cur + [i], i + 1, kidx + 1)
#         return 