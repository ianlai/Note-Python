class Solution:
    
    # DP Tabulation (2D array, 0/1 Knapsack problem) [O(N*S), 15%]
    # 0 [1, 0, 0, 0, 0, 0]
    # 1 [1, 1, 1, 1, 1, 1]
    # 2 [1, 1, 2, 2, 3, 3]
    # 5 [1, 1, 2, 2, 3, 4]
    
    def change(self, amount: int, coins: List[int]) -> int:
        print("DP (2D array), 0/1 Knapsack problem")
        if not coins and amount == 0:
            return 1
        if not coins and amount != 0:
            return 0
        
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1 
        coinsWithNone = [0] + coins
            
        for i in range(1, len(coinsWithNone)):
            for j in range(amount + 1):
                dp[i][j] = dp[i-1][j]
                if j - coinsWithNone[i] >= 0:
                    dp[i][j] += dp[i][j-coinsWithNone[i]]  #KEY: You can repeatedly use the coin 
      
        # Debug
        # for i in range(len(coinsWithNone)):
        #     print(coinsWithNone[i], dp[i])
        
        return dp[-1][-1] 
    
    # =====================================================================================
    
    # DP Tabulation [O(N*S), 94%]
    # >> iterative len(coins) times, order sensative
    
    # dp[i] += dp[i - coin] 
    # e.g. amount = 11, coins [2, 5, 10]
    # dp[10] = 0                                                    //use no coins
    # dp[10] = dp[10] (use no coins)   + dp[5] (use [2] cent)       //use [2] cent
    # dp[10] = dp[10] (use [2] cent)   + dp[5] (use [2,5] cent)     //use [2,5] cent 
    # dp[10] = dp[10] (use [2,5] cent) + dp[5] (use [2,5,10] cent)  //use [2,5,10] cent 
    
    def change1(self, amount: int, coins: List[int]) -> int:
        print("DP (1D array), solution approach")
        if not coins and amount == 0:
            return 1
        if not coins and amount != 0:
            return 0
        
        dp = [0] * (amount + 1)
        dp[0] = 1
            
        for coin in coins:  #This needs to be outside (order matters)
            for i in range(coin, amount + 1):        
                dp[i] += dp[i - coin]
                
        print(dp)
        return dp[amount]   #Use [2,5,10] cent