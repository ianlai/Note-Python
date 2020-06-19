class Solution:
    
    # Greedy Enumeration (go down faster) [96%]
    def numSquares(self, n):
        print("Greedy Enumeration (Solution)")
        def is_divided_by(n, count):
            """
                return: true if "n" can be decomposed into "count" number of perfect square numbers.
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums
            
            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    
        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count
    
    #===========================================
        
    # Bottom-up DP (Solution) [O(N*sqrtN), 44%]
    def numSquares2(self, n):
        print("Bottom-Up DP (Solution)")
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]
    
    #===========================================

    # Bottom-up DP [O(N*sqrtN), 58%]
    def numSquares2(self, n: int) -> int:
        print("Bottom-Up DP")
        if n == 1:
            return 1
        
        # Prepare the array for square numbers
        arr = []
        for e in range(1, n):
            if pow(e, 2) > n:
                break
            arr.append(pow(e, 2))
        
        # Initialization
        res = [0] * (n + 1)
        res[1] = 1 
        
        # DP loop 
        for i in range(2, n + 1):
            minValue = float('inf')
            for j in range(len(arr)):  #Loop all the number smaller than current   
                if arr[j] > i:
                    break
                idx = i - arr[j]
                if res[idx] < minValue:
                    minValue = res[idx]
                    res[i] = minValue + 1
        # Debug 
        # for i, v in enumerate(res):
        #     print(i, ":", v)
                    
        return res[n]
        
    #===========================================
    
    # Memoization [TLE]
    def numSquares2(self, n: int) -> int:
        print("Top-Down DP")
        if n == 1:
            return 1
        
        arr = []
        for e in range(1, n):
            if pow(e, 2) > n:
                break
            arr.append(pow(e, 2))
        #arr = arr[::-1]
        #print(arr)
        dic = {0:0, 1:1}
       
        ans = self.helper(arr, n, dic)
        #print(dic)
        return ans
        
    def helper(self, arr, target, memo):
        #print("target:", target, memo)
        if target == 0:
            return 0
        elif target == 1:
            return 1
        elif target < 0:
            return 99999
        
        if target in memo:
            return memo[target]
        
        minValue = float('inf')
        for i in range(len(arr)):
            minValue = min(minValue, 1 + self.helper(arr, target-arr[i], memo))
            
        memo[target] = minValue
        #print("**memo[target]:", memo[target])
        return memo[target]