class Solution:
    
    #Top-down (no memoization) -> TLE 
    def rob0(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        return self.helper0(nums, len(nums)-1)
    def helper0(self, nums, n):
        if n < 0 :
            return 0
        selectCur = nums[n] + self.helper0(nums, n-2)
        notSelectCur = self.helper0(nums, n-1)
        return max(selectCur, notSelectCur)
    
    #===============================================
    
    #Top-down (memoization, pass the memo down) -> TLE
    def rob1(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = [-1] * len(nums)
        return self.helper(nums, len(nums)-1, memo)
    def helper1(self, nums, n, memo):
        if n < 0:
            return 0
        if n == 0:
            return nums[0]
        if n == 1:
            if memo[1] == -1:
                memo[1] = max(nums[0], nums[1])
            return memo[1]
        
        selectCur = 0
        if memo[n-2] == -1:
            selectCur = nums[n] + self.helper1(nums, n-2, memo)
        else: 
            selectCur = nums[n] + memo[n-2]
        
        notSelectCur = 0
        if memo[n-1] == -1:
            notSelectCur = self.helper1(nums, n-1, memo)
        else: 
            notSelectCur = memo[n-1]

        return max(selectCur, notSelectCur)
    
    #===============================================
    
    #Top-down (memoization) 
    def rob2(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
    
        memo = [-1] * len(nums)
        def helper2(nums, n):
            if n < 0:
                return 0
            if n == 0:
                return nums[0]
            if n == 1:
                if memo[1] == -1:
                    memo[1] = max(nums[0], nums[1])
                return memo[1]

            selectCur = 0
            if memo[n-2] == -1:
                selectCur = nums[n] + helper2(nums, n-2)
            else: 
                selectCur = nums[n] + memo[n-2]

            notSelectCur = 0
            if memo[n-1] == -1:
                notSelectCur = helper2(nums, n-1)
            else: 
                notSelectCur = memo[n-1]

            return max(selectCur, notSelectCur)
        
        return helper2(nums, len(nums)-1)

        #===============================================
    
    #Buttom-Up 
    def rob(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[len(nums)-1]