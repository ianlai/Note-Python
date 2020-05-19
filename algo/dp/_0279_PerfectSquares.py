class Solution:
    
    # Bottom-up DP 
    def numSquares(self, n: int) -> int:
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
    
    # Memoization  
    def numSquares1(self, n: int) -> int:
        if n == 1:
            return 1
        
        arr = []
        for e in range(1, n):
            if pow(e, 2) > n:
                break
            arr.append(pow(e, 2))
        #arr = arr[::-1]
        print(arr)
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