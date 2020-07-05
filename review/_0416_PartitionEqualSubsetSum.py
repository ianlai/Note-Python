class Solution:
    
    # sum/2 = 11
    #      sum = 0  1  2  3  4  5  6  7  8  9  10 11         
    # id  num 
    # 0    x     1  0  0  0  0  0  0  0  0  0  0  0
    # 1    1     1  1  0  0  0  0  0  0  0  0  0  0   #0:  [0,0]=1       ; 1 : 0+1=1 
    # 2    5     1  1  0  0  0  1  1  0  0  0  0  0   #0,1:[1,0],[1,1]=1 ; 5 : 0+5=5; 6:1+5=6
    # 3   11     1  1  0  0  0  1  1  0  0  0  0  1   #...               ; 11: 0+11=11  
    # 4    5     1  1  0  0  0  1  1  0  0  0  1  1   #...               ; 10: 5+5=10  
    
    # Tabulation DP-4 (0/1 Knapsack with OR not Max) [14%]
    def canPartition(self, nums: List[int]) -> bool:
        print("Tabulation DP-4 (0/1 Knapsack with OR not Max) ")
        if not nums:
            return True
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        
        newNums = [0] + nums #0 is the no pickup case
        
        dp = [[0 for _ in range(s+1)] for _ in range(len(newNums))]
        dp[0][0] = 1 #no pickup, sum = 0
        
        for i in range(1, len(newNums)):  #First row is fixed: [1,0,0,0....]
            for j in range(s+1): 
                if j-newNums[i] >=0 :
                    #KEY: i in newNums can be used only ONCE, so dp[i-1][j-newNums[i]], not dp[i][j-newNums[i]]
                    #This is different from [518. Coin Change 2]
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-newNums[i]] 
                else:
                    dp[i][j] = dp[i-1][j]
        
        # Debug
        # for i in range(len(dp)):
        #     print('{:>2}'.format(newNums[i]), end=" ")
        #     print(dp[i])
        
        return dp[-1][-1]
            
    #=================================================
      
    # Memoization DP-3 (2 paths, return if each path is True, faster)  [80%]
    def canPartition3(self, nums: List[int]) -> bool:
        print("Memoization DP-3 (3 paths, return if each path is True, faster)")
        if not nums:
            return True
        s = sum(nums)
        if s % 2 == 1:
            return False
        ans = self.helper3(nums, 0, s//2, {})
        return ans

    def helper3(self, nums, start, target, memo):
        if start >= len(nums):
            return False

        if target in memo:
            return memo[target]

        if target < 0 :
            memo[target] = False
            return False 
        
        if target == 0:
            memo[target] = True
            return True

        if self.helper3(nums, start+1, target-nums[start], memo): #Use start
            memo[target] = True
            return True
        
        if self.helper3(nums, start+1, target, memo):   #Skip start
            memo[target] = True
            return True
        
        memo[target] = False
        return False
    
    #=================================================
    
    # Memoization DP-2 (3 paths, return if each path is True, faster) [80%]
    def canPartition2(self, nums: List[int]) -> bool:
        print("Memoization DP-2 (3 paths, return if each path is True, faster)")
        if not nums:
            return True
        s = sum(nums)
        if s % 2 == 1:
            return False
        ans = self.helper2(nums, 0, len(nums)-1, s//2, {})
        return ans

    def helper2(self, nums, start, end, target, memo):
        if start > end:
            return False
        
        # if (start, end, target) in memo:
        #     return memo[(start, end, target)]
        if target in memo:
            return memo[target]

        if target < 0 :
            #memo[(start, end, target)] = False
            memo[target] = False
            return False 
        if target == 0:
            # memo[(start, end, target)] = True
            memo[target] = True
            return True

        if self.helper2(nums, start+1, end, target-nums[start], memo): #Use start
            memo[target] = True
            return True
        
        if self.helper2(nums, start, end-1, target-nums[end], memo):   #Use end
            memo[target] = True
            return True
        
        if self.helper2(nums, start+1, end-1, target, memo):           #Skip start and end 
            memo[target] = True
            return True
        memo[target] = False
        return False
    
    #=================================================
    
    # Memoization DP-1 (return when all 3 paths completed, slow) [18%]
    def canPartition1(self, nums: List[int]) -> bool:
        print("Memoization DP-1 (return when all 3 paths completed, slow) ")
        if not nums:
            return True
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        
        memo = {}
        ans = self.helper1(nums, 0, len(nums)-1, target, memo)
        #print(memo)
        return ans
    
    def helper1(self, nums, start, end, target, memo):
        if start > end:
            return False
            
        # if (start, end, target) in memo:
        #     return memo[(start, end, target)]
        if target in memo:
            return memo[target]

        if target < 0 :
            #memo[(start, end, target)] = False
            memo[target] = False
            return False 
        if target == 0:
            # memo[(start, end, target)] = True
            memo[target] = True
            return True

        ans = False 
        ans |= self.helper1(nums, start+1, end, target-nums[start], memo) 
        ans |= self.helper1(nums, start, end-1, target-nums[end], memo)
        ans |= self.helper1(nums, start+1, end-1, target, memo)
        #memo[(start, end, target)] = ans
        memo[target] = ans
        return ans 