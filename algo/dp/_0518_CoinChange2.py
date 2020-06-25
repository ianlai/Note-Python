class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins and amount == 0:
            return 1
        if not coins and amount != 0:
            return 0
        
        dp = [0] * (amount + 1)
        # for coin in coins:
        #     if coin > amount:
        #         continue
        #     dp[coin] = 1 
        dp[0] = 1
            
        for coin in coins:
            for i in range(coin, amount + 1):        
                # if i - coin <= 0:
                #     continue
                dp[i] += dp[i - coin]
                
        print(dp)
        return dp[amount]