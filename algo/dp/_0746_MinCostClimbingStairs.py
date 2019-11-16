class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # dp(j) = min(cost[j] + dp(j-1), cost[j] + dp(j-2)) 
        
        if cost is None or len(cost) == 0: 
            return 0
        
        n = len(cost)
        dp = [-1] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n, 1):
            dp[i] = min(cost[i]+dp[i-1], cost[i]+dp[i-2])
        
        return min(dp[n-2], dp[n-1])