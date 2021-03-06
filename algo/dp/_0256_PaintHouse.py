class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        
        n = len(costs)
        if n == 1: #special case
            return min(costs[0])
        
        dp = [[0 for j in range(3)] for i in range(n)]
        #print(dp)
        #print(costs)
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        
        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]    
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        print(dp)
        return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])