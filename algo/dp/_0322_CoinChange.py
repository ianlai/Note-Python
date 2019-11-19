class Solution:
    
    #DP(memoization): 5% 
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins is None or len(coins) == 0 :
            return 0
        
        ans = self.dfs(coins, amount, {}) 
        if ans == float('inf'):
            return -1
        else:
            return ans
    
    def dfs(self, coins, amount, memo):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        
        minimum = float('inf')
        for i in range(len(coins)):
             minimum = min(minimum, 1 + self.dfs(coins, amount - coins[i], memo))
        memo[amount] = minimum 
        #print("amount:", amount, memo[amount])
        
        return memo[amount] 
            
    #=====================================================================
    #DFS: TLE
    def coinChange1(self, coins: List[int], amount: int) -> int:
        if coins is None or len(coins) == 0 :
            return 0
        ans = [float('inf')]
        self.dfs1(coins, amount, ans, [], 0)
        
        if ans[0] == float('inf'):
            return -1
        return ans[0]
            
    
    def dfs1(self, coins, amount, ans, cur, idx):
        print(amount, cur)
        if amount < 0:
            return 
        if amount == 0: 
            if len(cur) < ans[0]:
                ans[0] = len(cur)
            return 
        for i in range(idx, len(coins)):
            self.dfs1(coins, amount - coins[i], ans, cur + [coins[i]], i)
        
        