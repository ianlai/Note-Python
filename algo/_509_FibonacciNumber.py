# The iterative way to solve this problem is in _070_ClimbingStairs

class Solution:
    #recursion, memoization
    def fib(self, N: int) -> int:
        res = [-1] * (N+1)
        res[0] = 0
        if N == 0: 
            return res[0]
        res[1] = 1
        return self.helper(N, res)
    def helper(self, N: int, res: list) -> int:
        if res[N] == -1:
            res[N] = self.helper(N-1, res) + self.helper(N-2, res)
        return res[N]
    
    #recursion, no memoization
    def fibNoMemoization(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)