class Solution:
    
     # Bottom-Up DP [O(n2), 18%]
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True
        n = len(nums)
        dp = [-1] * n
        dp[0] = 1  #arrivable 
        for i in range(n):
            if dp[i] != 1:
                continue
            val = nums[i]
            boundary = min(i+val, n-1)
            #for j in range(i+1, boundary+1):
            for j in range(boundary, i, -1):
                if dp[j] != -1:
                    break
                dp[j] = 1
    
#         for i in range(1, n):
#             for j in range(i):
#                 if dp[j] == False:
#                     continue
#                 val = nums[j]
#                 for k in range(val, 0, -1):
#                     if j + k == i:
#                         dp[i] = True
#                         break
#                 if dp[i] == True:
#                     break
                
        return dp[-1] == True
        
    # ===========================================
    
    # Memoization DP [O(n2), TLE]
    def canJump1(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True
        print("len:", len(nums))
        return self.helper(nums, 0, set([]))
    
    def helper(self, nums, cur, memo):
        print("cur:", cur)
        if cur > len(nums) - 1:
            return False
        if cur == len(nums) - 1:
            return True
        if cur in memo:
            return False
        
        maxStep = nums[cur]
        print("maxStep:", maxStep)
        if maxStep == 0:
            return False
        #for i in range(1, maxStep+1):
        for i in range(maxStep, 0, -1):
            if self.helper(nums, cur + i, memo):
                return True
            memo.add(cur + i)
        return False
        