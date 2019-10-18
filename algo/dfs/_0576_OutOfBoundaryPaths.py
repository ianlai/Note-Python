class Solution:
    
    # Memoization
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if m <= 0 or n <= 0 or N <= 0:
            return 0
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0

        memo = [[[-1 for z in range(N+1)] for y in range(n)] for x in range(m)]   #i, j , N
        #print(memo)
        return self.dfs(memo, m, n, N, i, j) % (10 ** 9 + 7)
    
    def dfs(self, memo, m, n, N, i, j):
        #print(i, j, N)
        if self.isOut(m, n, i, j):
            return 1 
        if memo[i][j][N] != -1:
            return memo[i][j][N]
        if N != 0:
            memo[i][j][N] = self.dfs(memo, m, n, N-1, i-1, j  ) + self.dfs(memo, m, n, N-1, i+1, j  ) + self.dfs(memo, m, n, N-1, i  , j-1) + self.dfs(memo, m, n, N-1, i  , j+1)  
            return memo[i][j][N]
        return 0
    
    def isOut(self, m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return True
        return False
    
    # Pure DFS (too slow)
#     def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
#         if m <= 0 or n <= 0 or N <= 0:
#             return 0
#         if i < 0 or i >= m or j < 0 or j >= n:
#             return 0
        
#         ans = [0]
#         self.dfs(ans, m, n, N, i, j)
#         return ans[0]
    
#     def dfs(self, ans, m, n, N, i, j):
#         if self.isOut(m, n, i, j):
#             ans[0] += 1
#             return 
#         if N != 0:
#             self.dfs(ans, m, n, N-1, i-1, j  )
#             self.dfs(ans, m, n, N-1, i+1, j  )    
#             self.dfs(ans, m, n, N-1, i  , j-1)    
#             self.dfs(ans, m, n, N-1, i  , j+1)
#         return
    
#     def isOut(self, m, n, i, j):
#         if i < 0 or i >= m or j < 0 or j >= n:
#             return True
#         return False
        