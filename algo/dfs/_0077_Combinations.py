from typing import List
class Solution:
    #===================================
    ### Best (use different array in each level)
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
    
    #===================================
    ### OK (use cur one array to do the traverse, only clone to new in the end list())
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         if n == 0 or k == 0:
#             return []
#         ans = []
#         self.bfs(n, k, ans, [], 1)
#         return ans
    
#     def bfs(self, n, k, ans, cur, nidx):
#         if len(cur) == k:
#             #ans.append(list(cur))  #create new array
#             ans.append(cur[:])      #create new array
#             return 
#         for i in range(nidx, n + 1):
#             cur.append(i)
#             self.bfs(n, k, ans, cur, i + 1)
#             cur.remove(i)
#         return 
    
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

s = Solution()
print(s.combine(6,2))