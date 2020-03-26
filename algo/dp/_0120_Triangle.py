class Solution:
    
    #raw divide conquer -> O(2^n)
    #memoization        -> O(n^2)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0 :
            return 0
        return self.divideConquer(triangle, 0, 0, {})
    def divideConquer(self, t, x, y, memo):
        if x == len(t):
            return 0
        if (x,y) in memo:         #memoization
            return memo[(x,y)]
        
        minSub = min(self.divideConquer(t, x+1, y, memo), self.divideConquer(t, x+1, y+1, memo))
        memo[(x,y)] = minSub + t[x][y]
        return memo[(x,y)]
    
        