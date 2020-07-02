class Solution:
    
    # DP Tabulation [O(N*S), 94%]
    # >> iterative len(coins) times, order sensative
    
    # dp[i] += dp[i - coin] 
    # e.g. amount = 11, coins [1, 2, 5]
    # dp[10] = 0                                                    //use no coins
    # dp[10] = dp[10] (use no coins)   + dp[5] (use [2] cent)       //use [2] cent
    # dp[10] = dp[10] (use [2] cent)   + dp[5] (use [2,5] cent)     //use [2,5] cent 
    # dp[10] = dp[10] (use [2,5] cent) + dp[5] (use [2,5,10] cent)  //use [2,5,10] cent 
    
    def change(self, amount: int, coins: List[int]) -> int:
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